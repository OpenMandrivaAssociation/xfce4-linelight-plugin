Summary:	Search plugin for Xfce panel
Name:		xfce4-linelight-plugin
Version:	0.1.6
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		https://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	pkgconfig(thunarx-2)
Requires:	xfce4-panel-devel >= 4.4.2

%description
Linelight is a simple frontend for the locate search.
The search results are listed in sections (music, video, 
images, ... ) and can be executed directly from the 
Xfce panel.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_libdir}/xfce4/panel-plugins/%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/xfce4/panel-plugins/linelight.desktop
