Name:           mpvqt
Version:        1.0.0
Release:        1
Group:          Multimedia/Video
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only OR MIT
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/stable/mpvqt/mpvqt-%{version}.tar.xz
 
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(mpv)
 
%description
MpvQt is a libmpv wrapper for Qt Quick 2/Qml.
 
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Quick)
Requires:       pkgconfig(mpv)

%description devel
Development headers and link library for building packages which use %{name}.
 
%prep
%autosetup -p1
 
%build
%cmake
%make_build
 
%install
%make_install -C build
 
%files
%license LICENSES/LGPL* LICENSES/LicenseRef-KDE*
%doc README.md
%{_libdir}/libMpvQt.so.1{,.*}
 
%files devel
%{_includedir}/MpvQt/
%{_libdir}/libMpvQt.so
%{_libdir}/cmake/MpvQt/
