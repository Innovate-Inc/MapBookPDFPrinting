
***10/29/2013***
Code updated to support printing map books at ArcServer 10.1

This folder and it's contents should be accessible to ArcServer. Before creating a geoprocessing service ensure the folder has appropriate file system permissions for the ArcServer account.  Also, from AcrCatalog be sure to set this folder as a Registered Folder (Right click on the administrative server connection, server properties.  Go to the Data Store tab and add the folder and validate.)

Creating a Geoprocessing Service:
1) First w/in the script, set the path to the mxd files to the correct folder layout on the server.  Refer to line 27 w/in the script for notation.
2)At 10.1 the toolbox script needs to first be run via ArcCatalog.  The settings chosen will become the default settings for the service.  After the script runs sucesfully, open the Geoprocessing Results window and share/publish the results with ArcServer.  That's it!

