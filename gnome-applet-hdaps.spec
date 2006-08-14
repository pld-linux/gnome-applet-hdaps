%define		_realname	gnome-hdaps-applet
%define		_snap		20060120
Summary:	GNOME-based panel applet for monitoring the HDAPS protection status 
Name:		gnome-applet-hdaps
Version:	0.1.%{_snap}
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.zen24593.zen.co.uk/hdaps/%{_realname}-%{_snap}.tar.gz
# Source0-md5:	43ff308ccf5d15625e9f8f157bfc4bbc
URL:		http://www.zen24593.zen.co.uk/hdaps/
BuildRequires:	automake
#uildRequires:	
BuildRequires:	gnome-desktop-devel >= 2.4.0
BuildRequires:	gtkxmhtml-devel
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	intltool >= 0.21
BuildRequires:	gnome-libs-devel >= 1.4.2
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgtop-devel >= 2.10.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitors the /sys/block/xxx/queue/protect file and displays a graphical
representation of the HDAPS protection status. Looks for the protect
file under hda and sda and will use whichever is found first 
(lame but works for now).

%prep

%setup -q -c

%build

gcc $(pkg-config --cflags --libs libpanelapplet-2.0) -o gnome-hdaps-applet gnome-hdaps-applet.c


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/bonobo/servers/,%{_pixmapsdir}/%{_realname}}
install %{_realname}  $RPM_BUILD_ROOT%{_bindir}
install *.png  $RPM_BUILD_ROOT%{_pixmapsdir}/%{_realname}
install *.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers

##%%find_lang hdaps-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{_realname}.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall %{_realname}.schemas

%postun
%scrollkeeper_update_postun

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{_realname}
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/%{_realname}
%{_pixmapsdir}/%{_realname}/*.png
