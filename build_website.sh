# You may need to change ulimit due to tiles data that overload the limit to concurrent files opened
# For a temporary ulimit change, see http://serverfault.com/questions/389114/centos-redhat-change-open-files-ulimit-without-reboot
gitbook build --config book.json
find _book -type f -print0 | xargs -0 sed -i 's/Published using GitBook NPM module/Published using GitBook NPM module NPM module/g'
find _book -type f -print0 | xargs -0 sed -i 's/https:\/\/www.gitbook.com/https:\/\/github.com\/GitbookIO\/gitbook/g'
cp -R openlayers_book_samples _book/