<?xml version="1.0"?>
<rss version="2.0">
	<channel>
		<title>{{title}}</title>
		<link>{{link}}</link>
		<description>{{description}}</description>
		<language>{{lang}}</language>
		<copyright>{{copyright}}</copyright>
		<pubDate>{{pub_date}}</pubDate>
 
		<lastBuildDate>{{last_build_date}}</lastBuildDate>
		<docs>http://feed2.w3.org/docs/rss2.html</docs>
		<generator>Feeds RSS Crawler 1.0: {{parser}}</generator>
		<webMaster>kb.chernenko@gmail.com</webMaster>

		<image>
			<url>{{image}}</url>
			<title>{{title}}</title>
			<link>{{link}}</link>
		</image>

		%for item in items:
			<item>
				<title>{{item['title']}}</title>
				<link>{{item['link']}}</link>
				<description><![CDATA[
					<base href="{{link}}">
						{{item['description']}}
					</base>
				]]></description>
				<guid isPermaLink="true">{{item['guid']}}</guid>
				<pubDate>{{pub_date}}</pubDate>
			</item>
		%end
	</channel>
</rss>