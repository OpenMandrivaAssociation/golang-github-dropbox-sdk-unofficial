# Run tests in check section
%bcond_without check

%global goipath         github.com/dropbox/dropbox-sdk-go-unofficial
Version:                4.1.0

%global common_description %{expand:
An UNOFFICIAL Dropbox v2 API SDK for Go.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        An UNOFFICIAL Dropbox v2 API SDK for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4.1.0-1
- First package for Fedora

