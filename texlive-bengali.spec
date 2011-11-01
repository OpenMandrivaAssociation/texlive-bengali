Name:		texlive-bengali
Version:	20110108
Release:	1
Summary:	Support for the Bengali language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/bengali/pandey
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in
Devanagari. The package also supports Assamese.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bengali/bn.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnbanjon.mf
%{_texmfdistdir}/fonts/source/public/bengali/bndigit.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnjuk.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnkaar.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnlig.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnligtbl.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmacro.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmisc.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnpunct.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnswar.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsupp.mf
%{_texmfdistdir}/fonts/tfm/public/bengali/bnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/bnsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnsl10.tfm
%{_texmfdistdir}/tex/latex/bengali/beng.sty
%{_texmfdistdir}/tex/latex/bengali/ubn.fd
%{_texmfdistdir}/tex/latex/bengali/ubnx.fd
%doc %{_texmfdistdir}/doc/fonts/bengali/README
%doc %{_texmfdistdir}/doc/fonts/bengali/bengdoc.bn
%doc %{_texmfdistdir}/doc/fonts/bengali/bengdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/bengali/example.bn
%doc %{_texmfdistdir}/doc/fonts/bengali/example.pdf
%doc %{_texmfdistdir}/doc/fonts/bengali/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/bengali/beng.c

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
