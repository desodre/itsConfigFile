import os,yaml,argparse

class configFile:
    def __init__(self,finalPath:str = os.getcwd(), dut:str = None, tablet:str = None, fileName:str = 'config.yml'):
        self.finalPath = finalPath
        self.fileName = fileName
        self.data = ''
        self.setVariables(dut, tablet)
    
    def setVariables(self,dut:str,tablet:str = None): 
        dataPattern = {
            'TestBeds': [
            {
                'Name': 'TEST_BED_TABLET_SCENES',
                'Controllers': {
                'AndroidDevice': [
                    {'serial': 'ZY22L93QHJ', 'label': 'dut'},
                    {'serial': 'R9XY205RZRM', 'label': 'tablet'}
                ]
                },
                'TestParams': {
                'brightness': 192,
                'chart_distance': 20.0,
                'debug_mode': 'False',
                'lighting_cntl': 'arduino',
                'lighting_ch': 1,
                'camera': 0,
                'scene': '<scene-name>',
                'foldable_device': 'False'
                }
            },
            {
                'Name': 'TEST_BED_SENSOR_FUSION',
                'Controllers': {
                'AndroidDevice': [
                    {'serial': 'ZY22L93QHJ', 'label': 'dut'}
                ]
                },
                'TestParams': {
                'fps': 30,
                'img_size': '640,480',
                'test_length': 7,
                'debug_mode': 'False',
                'chart_distance': 25,
                'rotator_cntl': 'arduino',
                'rotator_ch': 1,
                'camera': 0,
                'foldable_device': 'False',
                'tablet_device': 'False',
                'lighting_cntl': 'arduino',
                'lighting_ch': 1,
                'scene': 'checkerboard'
                }
            },
            {
                'Name': 'TEST_BED_GEN2',
                'Controllers': {
                'AndroidDevice': [
                    {'serial': 'N1VT4B0122', 'label': 'dut'}
                ]
                },
                'TestParams': {
                'debug_mode': 'False',
                'chart_distance': 30,
                'rotator_cntl': 'gen2_rotator',
                'rotator_ch': '<controller-channel>',
                'camera': '<camera-id>',
                'foldable_device': 'False',
                'tablet_device': 'False',
                'lighting_cntl': 'gen2_lights',
                'lighting_ch': '<controller-channel>',
                'scene': 'scene_ip'
                }
            }
            ]
        }
        
        dataPattern['TestBeds'][0]['Controllers']['AndroidDevice'][0]['serial'] = dut
        if tablet:
            dataPattern['TestBeds'][0]['Controllers']['AndroidDevice'][1]['serial'] = tablet
            
        self.data = dataPattern
            
            
    
    def saveFile(self):
        with open(os.path.join(self.finalPath,self.fileName), 'w') as file:
            yaml.dump(self.data, file, default_flow_style=False)
        
    
def main():
    parser = argparse.ArgumentParser(description='Generate a YAML config file for test beds.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d','--dut', type=str, required=True, help='Serial number of the DUT device.')
    parser.add_argument('-t','--tablet', type=str, help='Serial number of the tablet device (optional).')
    parser.add_argument('-o','--output', type=str, default='config.yml', help='Output file path for the YAML config.')
    parser.add_argument('-p','--path', type=str, default=os.getcwd(), help='Path to save the config file. Default is current working directory.')
    
    args = parser.parse_args()
    args = parser.parse_args()
    config = vars(args)
    
    print("Generating config file with the following parameters:")
    print(f"DUT: {config['dut']}")
    if config['tablet']:
        print(f"Tablet: {config['tablet']}")
    print(f"File path: {os.path.join(config['path'], config['output'])}")
    
    configFile(finalPath=config['path'], dut=config['dut'], tablet=config['tablet'], fileName=config['output']).saveFile()
    
    

if __name__ == "__main__":
    main()
    
