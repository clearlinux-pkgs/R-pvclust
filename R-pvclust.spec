#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pvclust
Version  : 2.0.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/pvclust_2.0-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pvclust_2.0-0.tar.gz
Summary  : Hierarchical Clustering with P-Values via Multiscale Bootstrap
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
assessing the uncertainty in hierarchical cluster analysis.
             It provides AU (approximately unbiased) p-value as well as
             BP (bootstrap probability) value for each cluster in a dendrogram.

%prep
%setup -q -c -n pvclust

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552782698

%install
export SOURCE_DATE_EPOCH=1552782698
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pvclust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pvclust
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pvclust
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pvclust || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pvclust/DESCRIPTION
/usr/lib64/R/library/pvclust/INDEX
/usr/lib64/R/library/pvclust/Meta/Rd.rds
/usr/lib64/R/library/pvclust/Meta/data.rds
/usr/lib64/R/library/pvclust/Meta/features.rds
/usr/lib64/R/library/pvclust/Meta/hsearch.rds
/usr/lib64/R/library/pvclust/Meta/links.rds
/usr/lib64/R/library/pvclust/Meta/nsInfo.rds
/usr/lib64/R/library/pvclust/Meta/package.rds
/usr/lib64/R/library/pvclust/NAMESPACE
/usr/lib64/R/library/pvclust/R/pvclust
/usr/lib64/R/library/pvclust/R/pvclust.rdb
/usr/lib64/R/library/pvclust/R/pvclust.rdx
/usr/lib64/R/library/pvclust/data/lung.RData
/usr/lib64/R/library/pvclust/help/AnIndex
/usr/lib64/R/library/pvclust/help/aliases.rds
/usr/lib64/R/library/pvclust/help/paths.rds
/usr/lib64/R/library/pvclust/help/pvclust.rdb
/usr/lib64/R/library/pvclust/help/pvclust.rdx
/usr/lib64/R/library/pvclust/html/00Index.html
/usr/lib64/R/library/pvclust/html/R.css
