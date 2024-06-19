# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W1503


"attributes"


import unittest


from nixt.srv.opm import Parser


class TestAttrs(unittest.TestCase):

    def test_attrs(self):
        res = Parser.parse(TXT, "outline")
        self.assertTrue(len(res) == 50)


TXT = """
<?xml version='1.0' encoding='UTF-8' ?>
<opml version="1.0">
	<head>
		<title>Export from Plenary</title>
		<url>https://play.google.com/store/apps/details?id=com.spians.plenary</url>
		<ownerName>Spians Labs</ownerName>
		<ownerEmail>info@spianslabs.com</ownerEmail>
	</head>
	<body>
		<outline text="Better Programming - Medium" title="Better Programming - Medium" description="Advice for programmers. - Medium" xmlUrl="https://medium.com/feed/better-programming" type="rss" />
		<outline text="Code as Craft" title="Code as Craft" description="The Engineering Blog from Etsy" xmlUrl="https://codeascraft.com/feed/atom/" type="rss" />
		<outline text="CodeNewbie" title="CodeNewbie" description="Stories and interviews from people on their coding journey." xmlUrl="http://feeds.codenewbie.org/cnpodcast.xml" type="rss" />
		<outline text="Coding Horror" title="Coding Horror" description="programming and human factors" xmlUrl="https://feeds.feedburner.com/codinghorror" type="rss" />
		<outline text="Complete Developer Podcast" title="Complete Developer Podcast" description="A podcast by coders for coders about all aspects of life as a developer." xmlUrl="https://completedeveloperpodcast.com/feed/podcast/" type="rss" />
		<outline text="Dan Abramov's Overreacted Blog RSS Feed" title="Dan Abramov's Overreacted Blog RSS Feed" description="Personal blog by Dan Abramov. I explain with words and code." xmlUrl="https://overreacted.io/rss.xml" type="rss" />
		<outline text="Developer Tea" title="Developer Tea" description="Developer Tea exists to help driven developers connect to their ultimate purpose and excel at their work so that they can positively impact the people they influence. With over 13 million downloads to date, Developer Tea is a short podcast hosted by Jonathan Cutrell (@jcutrell), co-founder of Spec and Director of Engineering at PBS. We hope you'll take the topics from this podcast and continue the conversation, either online or in person with your peers. Twitter: @developertea :: Email: developertea@gmail.com" xmlUrl="https://feeds.simplecast.com/dLRotFGk" type="rss" />
		<outline text="English (US)" title="English (US)" description="Information from Twitter's engineering team about our tools, technology and services." xmlUrl="https://blog.twitter.com/engineering/en_us/blog.rss" type="rss" />
		<outline text="FLOSS Weekly (Audio)" title="FLOSS Weekly (Audio)" description="We're not talking dentistry here; FLOSS all about Free Libre Open Source Software. Join host Doc Searls and his rotating panel of co-hosts every Wednesday as they talk with the most interesting and important people in the Open Source and Free Software community. Records live every Wednesday at 12:30pm Eastern / 9:30am Pacific / 16:30 UTC." xmlUrl="https://feeds.twit.tv/floss.xml" type="rss" />
		<outline text="Facebook Engineering" title="Facebook Engineering" description="Facebook Engineering Blog" xmlUrl="https://engineering.fb.com/feed/" type="rss" />
		<outline text="GitLab" title="GitLab" description="" xmlUrl="https://about.gitlab.com/atom.xml" type="rss" />
		<outline text="Google Developers Blog" title="Google Developers Blog" description="Blog of our latest news, updates, and stories for developers" xmlUrl="http://feeds.feedburner.com/GDBcode" type="rss" />
		<outline text="Google TechTalks" title="Google TechTalks" description="" xmlUrl="https://www.youtube.com/feeds/videos.xml?user=GoogleTechTalks" type="rss" />
		<outline text="HackerNoon.com - Medium" title="HackerNoon.com - Medium" description="Elijah McClain, George Floyd, Eric Garner, Breonna Taylor, Ahmaud Arbery, Michael Brown, Oscar Grant, Atatiana Jefferson, Tamir Rice, Bettie Jones, Botham Jean - Medium" xmlUrl="https://medium.com/feed/hackernoon" type="rss" />
		<outline text="Hanselminutes with Scott Hanselman" title="Hanselminutes with Scott Hanselman" description="Hanselminutes is Fresh Air for Developers. A weekly commute-time podcast that promotes fresh technology and fresh voices. Talk and Tech for Developers, Life-long Learners, and Technologists." xmlUrl="https://feeds.simplecast.com/gvtxUiIf" type="rss" />
		<outline text="InfoQ" title="InfoQ" description="InfoQ feed" xmlUrl="https://feed.infoq.com" type="rss" />
		<outline text="Instagram Engineering - Medium" title="Instagram Engineering - Medium" description="Stories from the people who build @Instagram - Medium" xmlUrl="https://instagram-engineering.com/feed/" type="rss" />
		<outline text="Java, SQL and jOOQ." title="Java, SQL and jOOQ." description="Best Practices and Lessons Learned from Writing Awesome Java and SQL Code. Get some hands-on insight on what's behind developing jOOQ." xmlUrl="https://blog.jooq.org/feed" type="rss" />
		<outline text="JetBrains Blog" title="JetBrains Blog" description="Developer Tools for Professionals and Teams" xmlUrl="https://blog.jetbrains.com/feed" type="rss" />
		<outline text="Joel on Software" title="Joel on Software" description="" xmlUrl="https://www.joelonsoftware.com/feed/" type="rss" />
		<outline text="LinkedIn Engineering" title="LinkedIn Engineering" description="The official blog of the Engineering team at LinkedIn" xmlUrl="https://engineering.linkedin.com/blog.rss.html" type="rss" />
		<outline text="Martin Fowler" title="Martin Fowler" description="Master feed of news and updates from martinfowler.com" xmlUrl="https://martinfowler.com/feed.atom" type="rss" />
		<outline text="Netflix TechBlog - Medium" title="Netflix TechBlog - Medium" description="Learn about Netflix’s world class engineering efforts, company culture, product developments and more. - Medium" xmlUrl="https://netflixtechblog.com/feed" type="rss" />
		<outline text="Overflow - Buffer Resources" title="Overflow - Buffer Resources" description="In-depth ideas and guides to social media & online marketing strategy, published by the team at Buffer" xmlUrl="https://buffer.com/resources/overflow/rss/" type="rss" />
		<outline text="Podcast – Software Engineering Daily" title="Podcast – Software Engineering Daily" description="" xmlUrl="https://softwareengineeringdaily.com/category/podcast/feed" type="rss" />
		<outline text="Posts on &> /dev/null" title="Posts on &> /dev/null" description="Recent content in Posts on &> /dev/null" xmlUrl="https://www.thirtythreeforty.net/posts/index.xml" type="rss" />
		<outline text="Prezi Engineering - Medium" title="Prezi Engineering - Medium" description="The things we learn as we build our products - Medium" xmlUrl="https://engineering.prezi.com/feed" type="rss" />
		<outline text="Programming Throwdown" title="Programming Throwdown" description="Programming Throwdown educates Computer Scientists and Software Engineers on a cavalcade of programming and tech topics. Every show will cover a new programming language, so listeners will be able to speak intelligently about any programming language." xmlUrl="http://feeds.feedburner.com/ProgrammingThrowdown" type="rss" />
		<outline text="Programming – The Crazy Programmer" title="Programming – The Crazy Programmer" description="Programming, Design and Development" xmlUrl="https://www.thecrazyprogrammer.com/category/programming/feed" type="rss" />
		<outline text="Robert Heaton | Blog" title="Robert Heaton | Blog" description="Software engineer. One-track lover down a two-way lane" xmlUrl="https://robertheaton.com/feed.xml" type="rss" />
		<outline text="Scott Hanselman's Blog" title="Scott Hanselman's Blog" description="Scott Hanselman on Programming, User Experience, The Zen of Computers and Life in General" xmlUrl="http://feeds.hanselman.com/ScottHanselman" type="rss" />
		<outline text="Scripting News" title="Scripting News" description="It's even worse than it appears." xmlUrl="http://scripting.com/rss.xml" type="rss" />
		<outline text="Signal v. Noise" title="Signal v. Noise" description="Strong opinions and shared thoughts on design, business, and tech. By the makers (and friends) of <a href="https://www.basecamp.com" target="_blank" rel="noopener">Basecamp</a>. Since 1999." xmlUrl="https://m.signalvnoise.com/feed/" type="rss" />
		<outline text="Slack Engineering" title="Slack Engineering" description="" xmlUrl="https://slack.engineering/feed" type="rss" />
		<outline text="Software Defined Talk" title="Software Defined Talk" description="A weekly podcast covering all the news and events in Enterprise Software and Cloud Computing. We discuss topics including: Kubernetes, DevOps, Serverless, Security and Coding. Plus, plenty of off topic banter and nonsense to keep you entertained. Don't worry if you miss the latest industry conference, we will recap all the latest news from AWS, Microsoft Azure, Google Cloud Platform (GCP) and the Cloud Native Computing Foundation (CNCF)." xmlUrl="https://feeds.fireside.fm/sdt/rss" type="rss" />
		<outline text="Software Engineering Radio - The Podcast for Professional Software Developers" title="Software Engineering Radio - The Podcast for Professional Software Developers" description="Software Engineering Radio is a podcast targeted at the professional software developer. The goal is to be a lasting educational resource, not a newscast. Every 10 days, a new episode is published that covers all topics software engineering. Episodes are either tutorials on a specific topic, or an interview with a well-known character from the software engineering world. All SE Radio episodes are original content — we do not record conferences or talks given in other venues. Each episode comprises two speakers to ensure a lively listening experience. SE Radio is an independent and non-commercial organization. All content is licensed under the Creative Commons 2.5 license." xmlUrl="http://feeds.feedburner.com/se-radio" type="rss" />
		<outline text="SoundCloud Backstage Blog" title="SoundCloud Backstage Blog" description="SoundCloud's developer blog." xmlUrl="https://developers.soundcloud.com/blog/blog.rss" type="rss" />
		<outline text="Spotify Engineering" title="Spotify Engineering" description="Spotify’s official technology blog" xmlUrl="https://labs.spotify.com/feed/" type="rss" />
		<outline text="Stack Abuse" title="Stack Abuse" description="Learn Python, Java, JavaScript/Node, Machine Learning, and Web Development through articles, code examples, and tutorials for developers of all skill levels." xmlUrl="https://stackabuse.com/rss/" type="rss" />
		<outline text="Stack Overflow Blog" title="Stack Overflow Blog" description="Essays, opinions, and advice on the act of computer programming from Stack Overflow." xmlUrl="https://stackoverflow.blog/feed/" type="rss" />
		<outline text="The 6 Figure Developer" title="The 6 Figure Developer" description="Helping others reach their potential" xmlUrl="http://6figuredev.com/feed/rss/" type="rss" />
		<outline text="The Airbnb Tech Blog - Medium" title="The Airbnb Tech Blog - Medium" description="Creative engineers and data scientists building a world where you can belong anywhere. http://airbnb.io - Medium" xmlUrl="https://medium.com/feed/airbnb-engineering" type="rss" />
		<outline text="The Cynical Developer" title="The Cynical Developer" description="A UK based Technology and Software Developer Podcast that helps you to improve your development knowledge and career,
through explaining the latest and greatest in development technology and providing you with what you need to succeed as a developer." xmlUrl="https://cynicaldeveloper.com/feed/podcast" type="rss" />
		<outline text="The GitHub Blog" title="The GitHub Blog" description="Updates, ideas, and inspiration from GitHub to help developers build and design software." xmlUrl="https://github.blog/feed/" type="rss" />
		<outline text="The PIT Show: Reflections and Interviews in the Tech World" title="The PIT Show: Reflections and Interviews in the Tech World" description="This is the show where I sit down with people in the tech space and talk about what they are doing and how they get it all done." xmlUrl="https://feeds.transistor.fm/productivity-in-tech-podcast" type="rss" />
		<outline text="The Rabbit Hole: The Definitive Developer's Podcast" title="The Rabbit Hole: The Definitive Developer's Podcast" description="Welcome to The Rabbit Hole, the definitive developers podcast. If you are a software developer or technology leader looking to stay on top of the latest news in the software development world, or just want to learn actionable tactics to improve your day-to-day job performance, this podcast is for you." xmlUrl="http://therabbithole.libsyn.com/rss" type="rss" />
		<outline text="The Stack Overflow Podcast" title="The Stack Overflow Podcast" description="The Stack Overflow podcast is a weekly conversation about working in software development, learning to code, and the art and culture of computer programming. Hosted by Paul Ford and Ben Popper, the series features questions from our community, interviews with fascinating guests, and hot takes on what’s happening in tech. Founded in 2008, Stack Overflow is empowering the world to develop technology through collective knowledge. It’s best known for being the largest, most trusted online community for developers and technologists. More than 100 million people come to Stack Overflow every month to ask questions, help solve coding problems, and develop new skills." xmlUrl="https://feeds.simplecast.com/XA_851k3" type="rss" />
		<outline text="The Standup" title="The Standup" description="A podcast that delves into the obstacles and successes involved in creating, running, and sustaining successful software side projects." xmlUrl="https://feeds.fireside.fm/standup/rss" type="rss" />
		<outline text="The Women in Tech Show: A Technical Podcast" title="The Women in Tech Show: A Technical Podcast" description="A podcast about what we work on, not what it feels like to be a woman in tech. Hosted by Edaena Salinas, Software Engineer at Microsoft. Website: wit.fm" xmlUrl="https://thewomenintechshow.com/category/podcast/feed/" type="rss" />
		<outline text="programming" title="programming" description="Computer Programming" xmlUrl="https://www.reddit.com/r/programming/.rss" type="rss" />
	</body>
</opml>
"""