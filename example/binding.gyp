{
	'targets':[
		{
			'target_name':'example',
			'includes':['../nbind.gypi'],
			'sources':['Point.cc'],
			'xcode_settings':{
				'MACOSX_DEPLOYMENT_TARGET':'10.7',
				'OTHER_CFLAGS':[
					'-std=c++11',
					'-stdlib=libc++'
				]
			}
		}
	]
}