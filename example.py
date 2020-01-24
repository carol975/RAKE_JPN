from rake import Rake

rake = Rake()
text = "杉山古墳（すぎやまこふん）は、奈良県奈良市大安寺にある古墳。形状は前方後円墳。大安寺古墳群を構成する古墳の1つ。国の史跡に指定されている（史跡「大安寺旧境内 附 石橋瓦窯跡」のうち）。" 
print(rake.get_keywords(text,3))        

"""
Output Keyword List

['ぎやまこふん', '前方後円墳', '大安寺']
"""