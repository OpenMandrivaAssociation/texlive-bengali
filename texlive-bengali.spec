%global tl_name bengali
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Bengali language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/pandey
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in Devanagari.
The package also supports Assamese.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bengali
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/source/latex/bengali
%dir %{_datadir}/texmf-dist/tex/latex/bengali
%dir %{_datadir}/texmf-dist/fonts/source/public/bengali
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bengali
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/README
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/bengdoc.bn
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/bengdoc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/example.bn
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/example.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bengali/manifest.txt
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bn.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnbanjon.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bndigit.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnjuk.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnkaar.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnlig.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnligtbl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnmacro.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnmisc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnpunct.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/bnswar.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/xbnr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/xbnsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bengali/xbnsupp.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bengali/bnr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bengali/bnsl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bengali/xbnr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bengali/xbnsl10.tfm
%doc %{_datadir}/texmf-dist/source/latex/bengali/beng.c
%{_datadir}/texmf-dist/tex/latex/bengali/beng.sty
%{_datadir}/texmf-dist/tex/latex/bengali/ubn.fd
%{_datadir}/texmf-dist/tex/latex/bengali/ubnx.fd
