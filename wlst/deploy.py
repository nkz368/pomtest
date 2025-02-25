connect('weblogic', 'wls12345', 't3://155.248.161.146:7001')
# workspaceの場合
# deploy('pomtest', '/tmp/pomtest/target/pomtest.war', targets='AdminServer', upload='true')

# nexusの場合(直下にwgetでダウンロード)
deploy('pomtest', '/tmp/pomtest/pomtest.war', targets='AdminServer', upload='true')

disconnect()
exit()
