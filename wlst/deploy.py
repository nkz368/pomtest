connect('weblogic', 'wls12345', 't3://155.248.161.146:7001')
# deploy from workspace
# deploy('pomtest', '/tmp/pomtest/target/pomtest.war', targets='AdminServer', upload='true')

# deploy from nexus
deploy('pomtest', '/tmp/pomtest.war', targets='AdminServer', upload='true')

disconnect()
exit()
