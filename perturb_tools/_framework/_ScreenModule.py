
# _ScreenModule.py
__module_name__ = "_ScreenModule.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


import pandas as pd
import vintools as v
from anndata import AnnData

from ._supporting_functions._print_screen_object import _print_screen_object
from ._supporting_functions._data_reading._read_screen_from_PoolQ import _read_screen_from_PoolQ

from ._supporting_functions._fold_change import _fold_change
from ._supporting_functions._log_fold_change import _log_fold_change

from .._normalization._funcs._read_count_norm import _log_normalize_read_count


class _Screen:
    def __init__(self, X=None, *args, **kwargs):
        if X is not None:
            ad = AnnData(X, *args, **kwargs)
            self.X = ad.X
            self.guides = ad.obs
            self.condit = ad.var
            self.condit_m = ad.obsm
            self.condit_p = ad.obsp
            self.layers = ad.layers
            self.uns = ad.uns
            n_guides, n_conditions, _ = _print_screen_object(self)
            
    def __repr__(self) -> str:
        return _print_screen_object(self)[2]


    def read_PoolQ(self, path, metadata=False, merge_metadata_on='Condition'):

        """ """

        self._PoolQ_outpath = path
        self._PoolQScreenDict = _read_screen_from_PoolQ(self._PoolQ_outpath)
        
        for key, value in v.ut.update_dict(self._PoolQScreenDict).items():
            self.__setattr__(key, value)
        
        if metadata:
            self.condit = self.condit.merge(pd.read_csv(metadata), on=merge_metadata_on)
            
        _print_screen_object(self)
        
        
    def log_norm(self, layer_key='lognorm_counts'):
        
        self.layers[layer_key] = _log_normalize_read_count(self.X)
        
    
    def log_fold_change(self, cond1, cond2, lognorm_counts_key="lognorm_counts", name=False):

        """"""
        try:
            self.guides["{}_{}.lfc".format(cond1, cond2)] = _log_fold_change(
                self.layers[lognorm_counts_key], cond1, cond2
            )
        except:
            print("Calculating LFC against two previously calculated LFC values...")
            
            if not name:
                name = "{}_{}.dlfc".format(cond1.strip(".lfc"), cond2.strip(".lfc"))
            
            self.guides[name] = _log_fold_change(
                self.guides, cond1, cond2
            )
        
    def fold_change(self, cond1, cond2):

        """"""

        self.guides["{}_{}.fc".format(cond1, cond2)] = _fold_change(
            self.layers[lognorm_counts_key], cond1, cond2
        )
