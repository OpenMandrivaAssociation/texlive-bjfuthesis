%global tl_name bjfuthesis
%global tl_revision 59809

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.1
Release:	%{tl_revision}.1
Summary:	A thesis class for Beijing Forestry University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bjfuthesis
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bjfuthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bjfuthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a class file for producing dissertations and theses according to
the Beijing Forestry University (BJFU) Guidelines for Undergraduate
Theses and Dissertations. The class should meet all current requirements
and is updated whenever the university guidelines change.

