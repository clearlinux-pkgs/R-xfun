#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : R-xfun
Version  : 0.43
Release  : 80
URL      : https://cran.r-project.org/src/contrib/xfun_0.43.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xfun_0.43.tar.gz
Summary  : Supporting Functions for Packages Maintained by 'Yihui Xie'
Group    : Development/Tools
License  : MIT
Requires: R-xfun-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-xfun package.
Group: Libraries

%description lib
lib components for the R-xfun package.


%prep
%setup -q -n xfun
pushd ..
cp -a xfun buildavx2
popd
pushd ..
cp -a xfun buildavx512
popd
pushd ..
cp -a xfun buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711510692

%install
export SOURCE_DATE_EPOCH=1711510692
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/xfun/resources/record.css
/usr/lib64/R/library/xfun/resources/record.html
/usr/lib64/R/library/xfun/scripts/call-fun.R
/usr/lib64/R/library/xfun/scripts/child-pids.sh
/usr/lib64/R/library/xfun/tests/test-ci.R
/usr/lib64/R/library/xfun/tests/test-ci/test-cran.R
/usr/lib64/R/library/xfun/tests/test-ci/test-revcheck.R
/usr/lib64/R/library/xfun/tests/test-cran.R
/usr/lib64/R/library/xfun/tests/test-cran/test-base64.R
/usr/lib64/R/library/xfun/tests/test-cran/test-command.R
/usr/lib64/R/library/xfun/tests/test-cran/test-data-structure.R
/usr/lib64/R/library/xfun/tests/test-cran/test-encoding.R
/usr/lib64/R/library/xfun/tests/test-cran/test-io.R
/usr/lib64/R/library/xfun/tests/test-cran/test-json.R
/usr/lib64/R/library/xfun/tests/test-cran/test-knitr.R
/usr/lib64/R/library/xfun/tests/test-cran/test-markdown.R
/usr/lib64/R/library/xfun/tests/test-cran/test-packages.R
/usr/lib64/R/library/xfun/tests/test-cran/test-paths.R
/usr/lib64/R/library/xfun/tests/test-cran/test-string.R
/usr/lib64/R/library/xfun/tests/test-cran/test-utils.R
/usr/lib64/R/library/xfun/tests/test-cran/test-yaml.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/xfun/libs/xfun.so
/V4/usr/lib64/R/library/xfun/libs/xfun.so
/VA/usr/lib64/R/library/xfun/libs/xfun.so
/usr/lib64/R/library/xfun/libs/xfun.so
