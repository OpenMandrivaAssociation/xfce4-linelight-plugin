Summary:	Search plugin for Xfce panel
Name:		xfce4-linelight-plugin
Version:	0.1.6
Release:	%mkrel 6
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel
BuildRequires:	thunar-devel
Requires:	xfce4-panel-devel >= 4.4.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_libdir}/xfce4/panel-plugins/%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/xfce4/panel-plugins/linelight.desktop
