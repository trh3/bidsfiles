import glob
import os
import pandas as pd
import parse


class BIDSFiles:
    def __init__(self, root_dir):
        files = glob.glob(os.path.join(root_dir, "**", "*"),recursive=True)
        images = [f for f in files if '.nii' in f]
        jsons = [f for f in files if '.json' in f]
        events = [f for f in files if 'events.tsv' in f]

        self.image_db = self.image_db_constructor(images)

    def image_db_constructor(self, image_filenames):
        bids_parse_string = "sub-{sub}_ses-{ses}_{tags}_{modality}_{filetype}"

        image_protodb = [parse.parse(format = bids_parse_string, string=os.path.basename(f)) for f in image_filenames]
        image_db = pd.DataFrame(image_protodb)
        image_db['filepath'] = image_filenames
        return image_db
