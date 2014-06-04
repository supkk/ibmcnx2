######
#  Create a backup of J2EE Security Roles
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#
#

import sys
import os
import ibmcnx.functions

# Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile("ibmcnx/loadCnxApps.py")

path = raw_input( "Please provide a path for your backup files: " )
ibmcnx.functions.checkBackupPath( path )

apps = AdminApp.list()
appsList = apps.split( lineSeparator )
for app in appsList:
    filename = path + "/" + app + ".txt"
    print "Backup of %(1)s security roles saved to %(2)s." % { "1" : app.upper(), "2": filename}
    my_file = open( filename, 'w' )
    my_file.write ( AdminApp.view( app, "-MapRolesToUsers" ) )
    my_file.flush
    my_file.close()