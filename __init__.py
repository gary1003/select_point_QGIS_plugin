# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectPoint
                                 A QGIS plugin
 This plugin will ask user to choose database file, then the table. Prompt user to select point on the layer then saved selected.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-13
        copyright            : (C) 2021 by Gary
        email                : b07501047@ntu.edu.tw
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SelectPoint class from file SelectPoint.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .select_point import SelectPoint
    return SelectPoint(iface)
