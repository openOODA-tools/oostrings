Name:           oostrings
Version:        0.1.0
Release:        1%{?dist}
Summary:        Scans binary binaries and memory dumps for printable UTF-8 and ASCII sequences.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oostrings
Source0:        oostrings-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oostrings is a sovereign, capability-bounded BINARY EXTRACTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oostrings
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oostrings-uninstall

%files
/usr/bin/oostrings
/usr/bin/oostrings-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
