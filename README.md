# datalake-repo

prep steps:
xattr -p com.apple.quarantine libclntsh.dylib


00c1;6366546e;Safari;5A07037D-500A-4308-9B7C-756A2E02690F
xattr -w com.apple.quarantine "00c1;6366546e;Safari;5A07037D-500A-4308-9B7C-756A2E02690F" *.dylib
xattr -w com.apple.quarantine "00c1;6366546e;Safari;5A07037D-500A-4308-9B7C-756A2E02690F" *.dylib

***************
GIT LFS for large files
$ git lfs track "*.psd"
#run from root repo it will add to .gitattributes
<!-- *.zip filter=lfs diff=lfs merge=lfs -text
*/instantclient_19_8/* filter=lfs diff=lfs merge=lfs -text
*.1 filter=lfs diff=lfs merge=lfs -text
*.dylib filter=lfs diff=lfs merge=lfs -text
*.jar filter=lfs diff=lfs merge=lfs -text -->
then do
$ git commit -m "add file.psd"
$ git push