#!/usr/bin/env python3
# coding: utf-8
"""
Assimilate Example - Custom Command Installer

Demonstrates how to programmatically register Custom Commands via the REST API.
This replaces the manual workflow of navigating to Preferences > Custom Commands
and entering each command's settings by hand.

Use Cases:
  - Automated deployment of command suites (e.g. S2ROTO, S2SLATE, S2LLM)
  - CI/CD pipelines that provision workstations
  - First-run setup for post-production facilities
  - Keeping custom command registrations in sync across multiple seats

Requirements:
  - Assimilate SCRATCH / Live FX 9.9+ with REST API enabled (port 8080)
  - Python 3.6+

Usage:
  python3 install-custom-commands.py [--host HOST] [--list] [--remove NAME]
"""

from __future__ import absolute_import
import argparse
import json
import os
import sys

# --- Low-level HTTP client (stdlib only, no dependencies) -----------------

try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import Request, urlopen, HTTPError, URLError


class CommandInstallerClient:
    """Minimal REST client for Custom Command management."""

    def __init__(self, host="http://localhost:8080/APIV2"):
        self.host = host.rstrip("/")

    def _request(self, method, path, body=None):
        url = "%s%s" % (self.host, path)
        data = json.dumps(body).encode("utf-8") if body else None
        req = Request(url, data=data, method=method)
        req.add_header("Content-Type", "application/json")
        try:
            resp = urlopen(req, timeout=10)
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw.strip() else {}
        except HTTPError as e:
            raw = e.read().decode("utf-8")
            try:
                err = json.loads(raw)
            except Exception:
                err = {"message": raw}
            raise RuntimeError("API %s %s -> %d: %s" % (method, path, e.code, err))

    def get_system(self):
        return self._request("GET", "/system")

    def list_commands(self):
        return self._request("GET", "/application/commands")

    def add_command(self, command):
        return self._request("POST", "/application/commands", command)

    def get_command(self, name):
        return self._request("GET", "/application/commands/%s" % name)

    def update_command(self, name, command):
        return self._request("PUT", "/application/commands/%s" % name, command)

    def remove_command(self, name):
        return self._request("DELETE", "/application/commands/%s" % name)


# --- Command Definitions -------------------------------------------------

# Each command suite can define its commands as plain dicts.
# This makes it trivial to version-control and deploy command registrations.

S2_COMMANDS = [
    {
        "name": "S2FRAMECHECK",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2FRAMECHECK/s2framecheck.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2SLATE",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2SLATE/s2slate.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2ROTO",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2ROTO/s2roto.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2ROTO-POSTRENDER",
        "type": "postrender",
        "file": "/Library/Application Support/RogueLabs/S2ROTO/s2roto-postrender.py",
        "interpreter": "python3",
        "arguments": '"$ARG1"',
        "wait_till_finished": False,
        "xml_export": "selection",
        "require_selection": False,
    },
    {
        "name": "S2LLM",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2LLM/s2llm.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2PROXY",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2PROXY/s2proxy.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2COMFY",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2COMFY/s2comfy.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2SPLAT",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2SPLAT/s2splat.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2QC",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2QC/s2qc.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2AUDIO",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2AUDIO/s2audio.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
    {
        "name": "S2RELIGHT",
        "type": "application",
        "file": "/Library/Application Support/RogueLabs/S2RELIGHT/s2relight.py",
        "interpreter": "python3",
        "arguments": '"$ARG1" "$ARG2"',
        "wait_till_finished": True,
        "xml_export": "selection",
        "require_selection": True,
    },
]


def print_commands(commands):
    """Pretty-print a list of commands."""
    if not commands:
        print("  (no commands registered)")
        return
    print("  %-20s %-12s %-6s %s" % ("NAME", "TYPE", "WAIT", "FILE"))
    print("  " + "-" * 70)
    for cmd in commands:
        name = cmd.get("name", "?")
        ctype = cmd.get("type", "application")
        wait = "yes" if cmd.get("wait_till_finished", True) else "no"
        fpath = cmd.get("file", "?")
        # Truncate long paths for display
        if len(fpath) > 40:
            fpath = "..." + fpath[-37:]
        print("  %-20s %-12s %-6s %s" % (name, ctype, wait, fpath))


def main():
    parser = argparse.ArgumentParser(
        description="Install or manage Custom Commands via the Assimilate REST API"
    )
    parser.add_argument(
        "--host", default="http://localhost:8080/APIV2",
        help="REST API base URL (default: http://localhost:8080/APIV2)"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List currently registered commands and exit"
    )
    parser.add_argument(
        "--remove", metavar="NAME",
        help="Remove a command by name and exit"
    )
    parser.add_argument(
        "--remove-all", action="store_true",
        help="Remove all S2 commands"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be installed without making changes"
    )
    args = parser.parse_args()

    client = CommandInstallerClient(host=args.host)

    # Verify connection
    try:
        info = client.get_system()
        version = info.get("version", "?")
        build = info.get("build", "?")
        print("  Connected: SCRATCH %s (build %s)" % (version, build))
    except Exception as e:
        print("  ERROR: Cannot connect to REST API at %s" % args.host)
        print("  %s" % e)
        print("")
        print("  Make sure SCRATCH/Live FX is running with the REST API enabled.")
        sys.exit(1)

    # List mode
    if args.list:
        print("")
        print("  Registered Custom Commands:")
        print("")
        try:
            result = client.list_commands()
            commands = result.get("commands", result) if isinstance(result, dict) else result
            print_commands(commands if isinstance(commands, list) else [])
        except Exception as e:
            print("  Error listing commands: %s" % e)
        return

    # Remove mode
    if args.remove:
        print("")
        print("  Removing command: %s" % args.remove)
        try:
            client.remove_command(args.remove)
            print("  Done.")
        except Exception as e:
            print("  Error: %s" % e)
        return

    # Remove all S2 commands
    if args.remove_all:
        print("")
        print("  Removing all S2 commands...")
        for cmd in S2_COMMANDS:
            try:
                client.remove_command(cmd["name"])
                print("    Removed: %s" % cmd["name"])
            except Exception:
                pass  # Command might not exist
        print("  Done.")
        return

    # Install mode (default)
    print("")
    print("  Installing %d Custom Commands..." % len(S2_COMMANDS))
    print("")

    installed = 0
    skipped = 0
    errors = 0

    for cmd in S2_COMMANDS:
        name = cmd["name"]

        # Verify the script file exists (if running locally)
        if not args.dry_run and os.path.exists(cmd["file"]):
            pass  # File exists locally
        elif not args.dry_run and not os.path.exists(cmd["file"]):
            print("  WARNING: %s not found at %s" % (name, cmd["file"]))
            print("           Command will be registered but may fail when invoked.")

        if args.dry_run:
            print("  [DRY RUN] Would install: %s -> %s" % (name, cmd["file"]))
            installed += 1
            continue

        try:
            result = client.add_command(cmd)
            print("  Installed: %-20s -> %s" % (name, cmd["file"]))
            installed += 1
        except RuntimeError as e:
            if "already exists" in str(e).lower() or "duplicate" in str(e).lower():
                # Try updating instead
                try:
                    result = client.update_command(name, cmd)
                    print("  Updated:   %-20s -> %s" % (name, cmd["file"]))
                    installed += 1
                except Exception as e2:
                    print("  ERROR:     %-20s %s" % (name, e2))
                    errors += 1
            else:
                print("  ERROR:     %-20s %s" % (name, e))
                errors += 1

    print("")
    print("  Results: %d installed, %d skipped, %d errors" % (installed, skipped, errors))

    if installed > 0 and not args.dry_run:
        print("")
        print("  Commands are now available in SCRATCH:")
        print("    Right-click shot -> Custom Commands -> [command name]")
        print("")
        print("  Post-render commands appear in Output Node settings.")


if __name__ == "__main__":
    main()
