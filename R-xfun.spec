#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xfun
Version  : 0.26
Release  : 48
URL      : https://cran.r-project.org/src/contrib/xfun_0.26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xfun_0.26.tar.gz
Summary  : Supporting Functions for Packages Maintained by 'Yihui Xie'
Group    : Development/Tools
License  : MIT
Requires: R-xfun-lib = %{version}-%{release}
Requires: R-mime
BuildRequires : R-mime
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-xfun package.
Group: Libraries

%description lib
lib components for the R-xfun package.


%prep
%setup -q -c -n xfun
cd %{_builddir}/xfun

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631636350

%install
export SOURCE_DATE_EPOCH=1631636350
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xfun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xfun
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xfun
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc xfun || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xfun/DESCRIPTION
/usr/lib64/R/library/xfun/INDEX
/usr/lib64/R/library/xfun/LICENSE
/usr/lib64/R/library/xfun/Meta/Rd.rds
/usr/lib64/R/library/xfun/Meta/features.rds
/usr/lib64/R/library/xfun/Meta/hsearch.rds
/usr/lib64/R/library/xfun/Meta/links.rds
/usr/lib64/R/library/xfun/Meta/nsInfo.rds
/usr/lib64/R/library/xfun/Meta/package.rds
/usr/lib64/R/library/xfun/Meta/vignette.rds
/usr/lib64/R/library/xfun/NAMESPACE
/usr/lib64/R/library/xfun/NEWS.md
/usr/lib64/R/library/xfun/R/xfun
/usr/lib64/R/library/xfun/R/xfun.rdb
/usr/lib64/R/library/xfun/R/xfun.rdx
/usr/lib64/R/library/xfun/doc/index.html
/usr/lib64/R/library/xfun/doc/xfun.R
/usr/lib64/R/library/xfun/doc/xfun.Rmd
/usr/lib64/R/library/xfun/doc/xfun.html
/usr/lib64/R/library/xfun/help/AnIndex
/usr/lib64/R/library/xfun/help/aliases.rds
/usr/lib64/R/library/xfun/help/paths.rds
/usr/lib64/R/library/xfun/help/xfun.rdb
/usr/lib64/R/library/xfun/help/xfun.rdx
/usr/lib64/R/library/xfun/html/00Index.html
/usr/lib64/R/library/xfun/html/R.css
/usr/lib64/R/library/xfun/scripts/call-fun.R
/usr/lib64/R/library/xfun/scripts/child_pids.sh
/usr/lib64/R/library/xfun/tests/test-all.R
/usr/lib64/R/library/xfun/tests/testit/test-base64.R
/usr/lib64/R/library/xfun/tests/testit/test-command.R
/usr/lib64/R/library/xfun/tests/testit/test-data-structure.R
/usr/lib64/R/library/xfun/tests/testit/test-encoding.R
/usr/lib64/R/library/xfun/tests/testit/test-io.R
/usr/lib64/R/library/xfun/tests/testit/test-json.R
/usr/lib64/R/library/xfun/tests/testit/test-markdown.R
/usr/lib64/R/library/xfun/tests/testit/test-packages.R
/usr/lib64/R/library/xfun/tests/testit/test-paths.R
/usr/lib64/R/library/xfun/tests/testit/test-string.R
/usr/lib64/R/library/xfun/tests/testit/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/xfun/libs/xfun.so
