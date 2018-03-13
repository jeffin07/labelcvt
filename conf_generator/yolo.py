import os
import glob

class Yolo:
	def __init__(self,clss):
		self.lines = list(tuple(open(os.getcwd()+'/conf_generator/yolo.cfg','r')))
		self.classes = clss
		self.max_batches = 2000
		self.output_filters = (clss + 5) * 5
		

	def set_root(self,root):
		self.root = root

	def set_server_path(self, svr):
		self.server_path = svr

	def set_maxbatches(self, mb):
		self.max_batches = mb

	def set_output_filters(self, filters):
		self.output_filters = filters
 
	def set_classses(sefl, clss):
		self.classes = clss


	def generate(self, path):
		self.lines[229] = 'classes={}\n'.format(self.classes)
		self.lines[223] = 'filters={}\n'.format(self.output_filters)
		self.lines[14] = 'max_batches = {}\n'.format(self.max_batches)

		with open(path+"/yolo_conf.cfg",'w') as f:
			f.write(''.join(line for line in self.lines))
			f.close()

	def generate_test_train_files(self,path,server_path="/home/ubuntu/packages/darknet/dataset"):

		file_train = open(path+'/train.txt', 'w')  
		file_test = open(path+'/test.txt', 'w')
		server_path = "/home/ubuntu/packages/darknet/dataset"
		percentage_test = 10
		# Populate train.txt and test.txt
		counter = 1  	
		index_test = round(100 / percentage_test)  
		for pathAndFilename in glob.iglob(os.path.join(path,"images","*.jpg")):  
		    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

		    if counter == index_test:
		        counter = 1
		        file_test.write(server_path + "/" + title + '.jpg' + "\n")
		    else:
		        file_train.write(server_path + "/" + title + '.jpg' + "\n")
		        counter = counter + 1


	def generate_data_file(self, path):

		with open(path+'/obj.data', 'w') as f:
			f.write('classes= {}\n'.format(self.classes))
			f.write('train = {}\n'.format(self.server_path+"/mix/train.txt"))
			f.write('valid = {}\n'.format(self.server_path+"/mix/test.txt"))
			f.write('names = {}\n'.format(self.server_path+"/mix/cat.names"))
			f.write('backup = {}'.format(self.server_path+"/mix/backup"))
