# GPU metrics from DCGM
import sys
sys.path.append('/usr/local/dcgm/bindings/python3')
import DcgmReader
import dcgm_fields
dr = None


def dcgm_gpustats():
  global dr
  gpustats = []
  if dr == None:
      dr = DcgmReader.DcgmReader(fieldIds=[dcgm_fields.DCGM_FI_DEV_MEM_COPY_UTIL, dcgm_fields.DCGM_FI_DEV_GPU_UTIL, dcgm_fields.DCGM_FI_DEV_POWER_USAGE, dcgm_fields.DCGM_FI_PROF_PCIE_TX_BYTES, dcgm_fields.DCGM_FI_PROF_PCIE_RX_BYTES, dcgm_fields.DCGM_FI_PROF_NVLINK_TX_BYTES, dcgm_fields.DCGM_FI_PROF_NVLINK_RX_BYTES], 
          updateFrequency=1000000, maxKeepAge=3600, ignoreList=[], fieldGroupName="aimdata")
  return dr.GetLatestGpuValuesAsFieldNameDict()
