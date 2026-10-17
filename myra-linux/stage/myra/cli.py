# -*- coding: utf-8 -*-
"""
MYRA CLI  v5  [pip-install safe]
==========================================
  myra          → app (no login, no access key)
  myra reset    → same as myra (kept for backward compatibility)
  myra upgrade  → same as myra (kept for backward compatibility)
  myra install  → Windows startup ON + abhi background (mini orb) mein chalu
  myra uninstall→ Windows startup OFF
  myra status   → startup status
  myra --background → window ke bina, sirf orb ke saath chalo
"""
import sys, os
from pathlib import Path

# Windows console/terminal codepage is often NOT UTF-8 (e.g. cp1252) -
# without this, the banner's box-drawing chars / emoji prints elsewhere
# in the app can raise UnicodeEncodeError and crash the launch.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ── sys.path fix ─────────────────────────────────────────────────────────────
_here      = Path(__file__).resolve().parent      # .../site-packages/myra/
_site_pkgs = _here.parent                          # .../site-packages/
for _p in [str(_site_pkgs), str(_here)]:
    if _p not in sys.path: sys.path.insert(0, _p)


def _color():
    try:
        from colorama import Fore, Style, init; init(autoreset=True); return Fore, Style
    except ImportError:
        class _N:
            def __getattr__(self,_): return ""
        c=_N(); return c,c

def show_banner():
    F,S = _color()
    print(f"""{F.MAGENTA}
==================================================
███╗   ███╗██╗   ██╗██████╗  █████╗
████╗ ████║╚██╗ ██╔╝██╔══██╗██╔══██╗
██╔████╔██║ ╚████╔╝ ██████╔╝███████║
██║╚██╔╝██║  ╚██╔╝  ██╔══██╗██╔══██║
██║ ╚═╝ ██║   ██║   ██║  ██║██║  ██║
╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝{S.RESET_ALL}
{F.CYAN}        MYRA AI ASSISTANT{S.RESET_ALL}
{F.GREEN}        by Vikash Kumar  @CodeNinjaVik{S.RESET_ALL}
{F.MAGENTA}=================================================={S.RESET_ALL}
""")

def _dirs():
    home=Path.home(); docs=home/"Documents"
    for d in [docs/"TITAN_Notes",docs/"TITAN_Recordings",docs/"TITAN_Wallpapers",
              docs/"TITAN_PDFs",home/"TITAN_Codes",home/"ARIA_Downloads",
              Path(os.environ.get("APPDATA",str(home/"AppData"/"Roaming")))/"MYRA"]:
        try: d.mkdir(parents=True, exist_ok=True)
        except Exception: pass

def _run_app() -> int:
    try:
        from Main_normal import main as run_app
    except ImportError as e:
        print(f"[MYRA] ❌ Main_normal not found: {e}", file=sys.stderr)
        return 1
    try:
        run_app()
    except Exception as e:
        print(f"[MYRA] App error: {e}", file=sys.stderr)
        import traceback; traceback.print_exc(); return 1
    return 0

def _launch() -> int:
    from myra.config import load_environment
    load_environment()
    _dirs()
    return _run_app()

def reset() -> int:
    show_banner()
    return _launch()

def upgrade() -> int:
    show_banner()
    return _launch()

def install_cmd() -> int:
    """`myra install` — Windows startup ON + MYRA ko abhi background (orb) mein chalu karo."""
    try:
        import myra_autostart as au
    except ImportError as e:
        print(f"[MYRA] autostart module nahi mila: {e}", file=sys.stderr)
        return 1
    ok = au.enable(True)
    print("[MYRA] ✅ Windows startup ON — PC start/restart par MYRA orb ke saath khud chalu hogi." if ok
          else "[MYRA] ❌ Startup ON nahi ho paya.")
    if ok:
        started = au.spawn_background()
        print("[MYRA] ✅ MYRA abhi background mein chalu ho gayi (screen par orb dikhega)." if started
              else "[MYRA] ⚠️  Abhi chalu nahi ho payi — `myra` command se chalao.")
    return 0 if ok else 1


def uninstall_cmd() -> int:
    """`myra uninstall` — Windows startup OFF."""
    try:
        import myra_autostart as au
    except ImportError as e:
        print(f"[MYRA] autostart module nahi mila: {e}", file=sys.stderr)
        return 1
    ok = au.disable()
    print("[MYRA] Windows startup OFF." if ok else "[MYRA] ❌ Startup OFF nahi ho paya.")
    return 0 if ok else 1


def status_cmd() -> int:
    try:
        import myra_autostart as au
        on = au.is_enabled()
        print(f"[MYRA] Windows startup: {'ON' if on else 'OFF'}")
        print(f"[MYRA] Registered command: {au.registered_command()}" if on else f"[MYRA] `myra install` se ye command register hogi: {au.launch_command(True)}")
    except ImportError as e:
        print(f"[MYRA] autostart module nahi mila: {e}")
    return 0


def main() -> int:
    show_banner()
    if len(sys.argv) > 1:
        a = sys.argv[1].lower()
        if a in ("install", "setup", "--install-startup"): return install_cmd()
        if a in ("uninstall", "--uninstall-startup"):      return uninstall_cmd()
        if a == "status":                                  return status_cmd()
        if a in ("reset","upgrade","re-activate"): return reset()
    return _launch()          # `myra --background` bhi yahin se: Main_normal flag padhta hai

if __name__ == "__main__":
    raise SystemExit(main())
