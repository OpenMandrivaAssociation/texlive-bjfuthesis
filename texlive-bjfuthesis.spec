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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a class file for producing dissertations and theses according to
the Beijing Forestry University (BJFU) Guidelines for Undergraduate
Theses and Dissertations. The class should meet all current requirements
and is updated whenever the university guidelines change.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bjfuthesis
%dir %{_datadir}/texmf-dist/tex/latex/bjfuthesis
%dir %{_datadir}/texmf-dist/doc/latex/bjfuthesis/documentation
%dir %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example
%dir %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/contents
%dir %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/bjfuthesis.layout
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/documentation/bjfuthesis.lyx
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/documentation/bjfuthesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/documentation/bjfuthesis.tex
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/bibliography.bib
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/contents/cover.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/contents/mission-statement.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/contents/statement-of-originality.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/admin-knowledge-graph.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/admin-movie.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/admin-navigation.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/anonymous-category.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/anonymous-details.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/anonymous-index.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/anonymous-search.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/enhanced-recommendation.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/general-details.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/illustration-of-ripple-sets.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/jwt.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/recommendation-procedure.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/ripplenet-framework.png
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/figures/use-case.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/thesis.lyx
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/thesis.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bjfuthesis/example/thesis.tex
%{_datadir}/texmf-dist/tex/latex/bjfuthesis/bjfuthesis.cls
