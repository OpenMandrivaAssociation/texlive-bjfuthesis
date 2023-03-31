Name:		texlive-bjfuthesis
Version:	59809
Release:	2
Summary:	A thesis class for Beijing Forestry University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bjfuthesis
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bjfuthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bjfuthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a class file for producing dissertations and theses
according to the Beijing Forestry University (BJFU) Guidelines
for Undergraduate Theses and Dissertations. The class should
meet all current requirements and is updated whenever the
university guidelines change.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bjfuthesis
%doc %{_texmfdistdir}/doc/latex/bjfuthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
