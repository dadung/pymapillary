#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This sample code gets image detections. I can't really test it because
# I don't have access to it.

from pymapillary import Mapillary

map = Mappilary("insert client id here")
raw_json = map.search_images_detections(bbox=bbox, per_page=per_page)
print(raw_json)

# Download the beautified json for debugging
return_json_file(raw_json, "../sample_json_output/search_images_example.json")
