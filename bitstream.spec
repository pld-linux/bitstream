Summary:	biTStream - set of C headers allowing a simple access to binary structures
Summary(pl.UTF-8):	biTStream - zbiór nagłówków C ułatwiających dostęp do struktur binarnych
Name:		bitstream
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	ftp://ftp.videolan.org/pub/videolan/bitstream/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	5ba0c96d6c7c9131ba60a9a8fc147556
URL:		http://www.videolan.org/developers/bitstream.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
biTStream is a set of C headers allowing a simpler access to binary
structures such as specified by MPEG, DVB, IETF, etc. It currently
implements the following specifications:
 - ISO/IEC 13818-1 (MPEG-2 systems)
 - ETSI EN 300 468 (Service Information in DVB systems)
 - IETF RFC 2550 (Real Time Protocol)
 - ETSI EN 50 221 (Common Interface Specification)
 - ETSI TS 103 194 (DVB Simulcrypt)
 
%description -l pl.UTF-8
biTStream to zbiór nagłówków C pozwalających na prosty dostęp do
binarnych struktur, takich jak definiowane przez MPEG, DVB, IETF itp.
Obecnie zaimplementowane są następujące specyfikacje:
 - ISO/IEC 13818-1 (systemy MPEG-2)
 - ETSI EN 300 468 (Service Information w systemach DVB)
 - IETF RFC 2550 (Real Time Protocol)
 - ETSI EN 50 221 (Common Interface Specification)
 - ETSI TS 103 194 (DVB Simulcrypt)

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO
%{_includedir}/bitstream