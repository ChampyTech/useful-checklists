# ✅ Dualbooting Checklist

↖️ [Return to the main file](../README.md)

### Preparation

- [ ] Backup all important data
- [ ] Check disk space (at least 20–30 GB free for the second OS)
- [ ] Download ISO files for both operating systems
- [ ] Create bootable USB drive(s) with Rufus, balenaEtcher, etc.

### BIOS/UEFI Configuration

- [ ] Boot into BIOS/UEFI
- [ ] Disable Secure Boot (if needed by second OS)
- [ ] Enable AHCI mode (for Linux compatibility)
- [ ] Set USB as first boot option temporarily

### Installation

- [ ] Boot from USB and start OS installer
- [ ] Choose “Install alongside” or manual partitioning
- [ ] Create separate partition(s) for the second OS
- [ ] Install bootloader (e.g. GRUB if Linux is second)

### Post-Install

- [ ] Reboot and test both operating systems
- [ ] Set default boot OS (via GRUB or BIOS)
- [ ] Update both systems after install
- [ ] Optional: Customize GRUB menu appearance or timeout
