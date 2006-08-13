%define		_realname	gnome-hdaps-applet
%define		_snap		20060120
Summary:	GNOME-based panel applet and management tool to manage wireless network cards 
Name:		gnome-applet-hdaps
Version:	%{_snap}
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.zen24593.zen.co.uk/hdaps/%{_realname}-%{version}.tar.gz
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
This project aims to create a GNOME-based panel applet and management
tool to manage wireless network cards that support Linux wireless
extensions.

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

# Restart GNOME and you should find the "HDAPS Status" applet in the "Add to Panel" dialog

##%%find_lang hdaps-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{_realname}
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/%{_realname}
%{_pixmapsdir}/%{_realname}/*.png
