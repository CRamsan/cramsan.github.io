# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages
# To run the server:
export PATH=~/.gem/ruby/2.3.0/bin:$PATH
bundle exec jekyll clean
bundle exec jekyll build --trace --lsi
