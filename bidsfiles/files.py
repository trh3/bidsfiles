import glob
import os
import pandas as pd
import parse
import logging


class BIDSFiles:
    def __init__(self, root_dir):
        logging.basicConfig(level  = 'INFO')
        files = glob.glob(os.path.join(root_dir, "**", "*"),recursive=True)
        images = [f for f in files if '.nii' in f]
        jsons = [f for f in files if '.json' in f]
        events = [f for f in files if 'events.tsv' in f]

        self.image_db = self.db_constructor(images)
        self.json_db = self.db_constructor(jsons)
        self.events_db = self.db_constructor(events)

    def db_constructor(self, image_filenames):
        image_protodb = [self.filename_parser(s) for s in image_filenames]
        image_db = pd.DataFrame(image_protodb)
        image_db['filepath'] = image_filenames
        return image_db

    def filename_parser(self, file_path):
        print(file_path)
        split = os.path.basename(file_path).split("_")
        tag_parse = "{key}-{value}"
        modality_parse = "{modality}.{file_ext}"
        tags = [parse.parse(format = tag_parse, string = s, evaluate_result=True).named for s in split[:-1] if
                parse.parse(format = tag_parse, string = s, evaluate_result=True) is not None]
        print(tags)
        modality = parse.parse(format = modality_parse, string = split[-1], evaluate_result=True).named
        tags = {d['key']:d['value'] for d in tags}
        if modality is not None:
            tags.update(modality)
        return tags

