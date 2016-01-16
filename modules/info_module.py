def info(object, spacing=10, collapse=1,html=False,file_name=None): 
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) ] #if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    if not html:
        print "\n".join(["%s %s" %
                          (method.ljust(spacing),
                           processFunc(str(getattr(object, method).__doc__)))
                         for method in methodList])
    else:
        
        table="<table class='table'><thead> Method name </thead><thead>Method description</thead><tbody>"
        for each in [   (
             method.ljust(spacing),
             processFunc(str(getattr(object, method).__doc__))
             )
             for method in methodList
        ]:
            method_name = each[0]
            method_description =each[1]
            table+="<tr><td>%s</td><td>%s</td>"%(method_name,method_description)
        table+="</tbody></table>"
        if not file_name:
            file_name="info.html"
        f=open(file_name,"w")
        html="""<html><head>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        </head><body>""" + table + """</body></html>"""
        f.write(html)
        f.close()