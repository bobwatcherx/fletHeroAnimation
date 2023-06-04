from flet import *


dog_url = "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcREj22c-wMNL5IDmU99v8G7voUl17Yxm0JJqMLqttdPT4DnaB99zqVK7HWiNzjP3aZnzCEf-ikAqb2yiDk"

def main(page:Page):

	page.window_width=300
	page.window_height=600
	page.padding = 0
	page.spacing = 0

	detailshow = False

	def switchscreen(e):
		detailshow = True
		# AND SHOW listdog
		# WITH EFFECT OPACITY AND MOVE TO TOP
		listdog.opacity = 0 if detailshow == True else 1
		listdog.offset = transform.Offset(0,0) if detailshow == True else transform.Offset(0,0)

		# AND FOR ctdetails WILL SHOW IF listdog hide
		ctdetails.opacity = 1 if detailshow == True else 0
		ctdetails.offset = transform.Offset(0,0) if detailshow == True else transform.Offset(1,0)

		page.update()


	# AND FOR BACK BUTTON
	def backbutton(e):
		detailshow = False
		# AND SHOW listdog
		# WITH EFFECT OPACITY AND MOVE TO TOP
		listdog.opacity = 0 if detailshow == True else 1
		listdog.offset = transform.Offset(0,0) if detailshow == True else transform.Offset(0,0)

		# AND FOR ctdetails WILL SHOW IF listdog hide
		ctdetails.opacity = 1 if detailshow == True else 0
		ctdetails.offset = transform.Offset(0,0) if detailshow == True else transform.Offset(1,0)

		page.update()



	
	# NOW I CREATE DETAILS SCREEN IF YOU CLICK CITNAINER
	# DOG
	ctdetails = Container(
		# THIS WILL HIDE 
		opacity=0,
		animate_opacity=100,
		offset=transform.Offset(1,0),
		animate_offset=animation.Animation(200,"easeIn"),
		content=Column([
			Stack([
				Container(
				border_radius=border_radius.only(bottom_left=30,bottom_right=30),
				content=Image(src=dog_url,
					fit="cover",
					width=page.window_width,
					height=300
					)
					),
				Container(
					padding=10,
					content=Row([
						IconButton(
							icon="arrow_back",
							on_click=backbutton,
							icon_color="white"
							),
						Text("Dog Details",
							weight="bold",
							size=25,
							color="white"
							)

						])

					)

				]),
			# AND CREATE DETAILS NAME
			Container(
				padding=10,
				content=Row([
					Text("My Dogs",
						weight="bold",
						size=25
						),
					Icon(name="favorite",
						size=30
						)
					],alignment="spaceBetween")

				)




			])

		)




	listdog = Card(
		elevation=10,
		margin=20,
		animate_opacity=100,
		offset=transform.Offset(0,0),
		animate_offset=animation.Animation(300,"easeIn"),
		content=Container(
			padding=10,
			# THIS WILL ENABLE RIPPLE EFEFCT 
			# IF YOU CLICK Container
			ink=True,
			width=page.window_width,
			bgcolor="white",
			on_click=switchscreen,
			content=Row([
				Image(src=dog_url,
					fit="cover",
					width=80,
					height=60
					),
				Text("my dogs",
					weight="bold",
					size=20
					)
				])
			)

		)

	page.add(
		Column([
			ctdetails,
			listdog
			])

		)

flet.app(target=main)
