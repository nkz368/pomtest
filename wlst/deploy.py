connect('weblogic', 'wls12345', 't3://155.248.161.146:7001')
deploy('pomtest', '/tmp/pomtest/target/pomtest.war', targets='AdminServer')

disconnect()
exit()
