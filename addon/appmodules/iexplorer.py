#appModules/iexplorer.py
class iexplorerunlabeleditem(UIA):
	def _get_name(self):
		objname = ''
		l = list()
		for x in self.children:
			objname = x.firstChild.name
			if objname != '': l.append(objname)
		s = ' '.join(l)
		return s

class  AppModule(appModuleHandler.AppModule):
		if obj.name == '':
			clslist.insert(0, iexplorerdetailsitem)
		elif obj.role == controlTypes.ROLE_TREEVIEWITEM: