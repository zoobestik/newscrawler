<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<title>Feeds Crawler List</title>
		<style type="text/css"></style>
	</head>
	<body>
		<ul>
			%for tpl_index, tpl_url in enumerate(urls):
				<li>
					<a href="/id{{tpl_index}}">RSS</a>&nbsp;(<a href="{{tpl_url['url']}}">{{tpl_url['url']}}</a>)
				</li>
			%end
		</ul>
	</body>
</html>