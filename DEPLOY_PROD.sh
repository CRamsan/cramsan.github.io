# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages
# To run the server:
bundle exec jekyll clean --dest tmp_site
bundle exec jekyll build --trace --lsi --dest tmp_site
rm -rf _site
mv tmp_site _site
