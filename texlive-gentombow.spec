Name:		texlive-gentombow
Version:	64333
Release:	1
Summary:	Generate Japanese-style crop marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gentombow
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentombow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gentombow.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides a LaTeX package for generating
Japanese-style crop marks (called 'tombow' in Japanese) for
practical use in self-publishing. The bundle contains the
following packages: gentombow.sty: Generate crop marks (called
'tombow' in Japanese) for practical use in self-publishing. It
provides the core 'tombow' feature if not available.
pxgentombow.sty: Superseded by gentombow.sty; kept for
compatibility only. bounddvi.sty: Set papersize special to DVI
file. Can be used on LaTeX/pLaTeX/upLaTeX (with DVI output
mode) with dvips or dvipdfmx drivers.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gentombow
%doc %{_texmfdistdir}/doc/latex/gentombow

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
