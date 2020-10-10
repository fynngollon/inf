cd ..
#!/PortableGit/bin/bach
cd inf
git add *
git commit -m "He double-clicked the magic batch! ($(date))"
git pull origin master
git push origin master --repo git@github.com:fynngollon/inf.git