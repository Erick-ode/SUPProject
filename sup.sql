SQLite format 3   @     V                                                               V .WJ�  ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               �k�)tableregisterregisterCREATE TABLE register (
	id INTEGER NOT NULL, 
	contact VARCHAR(50) NOT NULL, 
	channel VARCHAR(50) NOT NULL, 
	attendance VARCHAR(50) NOT NULL, 
	associate VARCHAR(50) NOT NULL, 
	demand VARCHAR(50) NOT NULL, 
	product_offer VARCHAR(3) NOT NULL, 
	product VARCHAR(50), 
	effective VARCHAR(3), 
	time_spent VARCHAR(50) NOT NULL, 
	time_hour VARCHAR(50) NOT NULL, 
	manager_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(manager_id) REFERENCES user (id)
)�M�}tableuseruserCREATE TABLE user (
	id INTEGER NOT NULL, 
	agency INTEGER, 
	login VARCHAR(100), 
	name VARCHAR(1000), 
	password VARCHAR(100), 
	admin BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (login)
)'; indexsqlite_autoindex_user_1user          K w�K��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      � {� v'�=eli@gmail.commoritasha256$2pNheH5Kh0B6bhR5$5cd0da69c21eeca99083f7d054553e516c3351b67b6c373d2d4b573daa8e9c0d   � 	G�=sandro.anjos.01@edu.unipar.brsandrosha256$IogttVomEn2jg6p2$0fb0120f4b193b4216ae0c402a2665cb16c035060dc   w+�=teste@gmail.comtestesha256$b7xiALkNlYrUhs7U$76c2e8763056bbdd41c0469003f412bc78fb3342b72754d6fd185cb36068ec79� 	K9�=gabriele_benitez@sicredi.com.brGabriele Tosti Benitezsha256$D6A4ZKS3QuRZMMeT$fc97a6fb11b5361390ed9ab70482ff248e5e1b08f94049541770975c7454b88e� 	C9�=	sandro_anjos@sicredi.com.brSandro Sousa dos Anjossha256$lNGOyBqkOdiJOwww$8308635f73835b6378cf23bc7292f8d0a211438a424e561e23990ada5b46f436� 	A%�=	erick_paula@sicredi.com.brErick Amaralsha256$N5vPvttRACvsLYyY$0ccef307f5abef17cdd2d903dd2366e4d15e6122f1846116bcde5eb0a4005f37
   � �����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             � vi� eli@gmail.com   'sandro.anjos.01   teste@gmail.com#Kgabriele_benitez@sicredi.com.brCsandro_anjos@sicredi.com.brA	erick_paula@sicredi.com.br	8 � ��<�Y���j
��U�
	���                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          k 39)#ReceptivoE-mailNegócioOutras cooperativasSeguros e previdênciaNãoAté 5 minutos12:00-15:00w 3!3)#ReceptivoWhatsappNegócioOutras cooperativasConsórcioSimDébito automáticoNãoAté 5 minutos10:00-12:00h -+#ReceptivoE-mailNegócioOutras carteirasCobrançaSimCobrançaNãoAté 15 minutos12:00-15:00
� e-'+#ReceptivoTelefoneServiçoOutras agênciasCobrançaSimInvestimentosSimAté 15 minutos10v 39!+#AtivoWhatsappServiçoOutras cooperativasSeguros e previdênciaSimConsórcioSimAté 15 minutos12:00-15:00{ -+13#ReceptivoVisitaNegócioOutras agênciasCanais digitaisSimCapital programadoNãoAcima de 15 minutos12:00-15:00k )?)#ReceptivoWhatsappDirecionamentoPoupadorRecuperação de créditoNãoAté 5 minutos12:00-15:00   k-;)#ReceptivoVisitaServiçoOutras agênciasConta corrente/PoupadorNãoAté 5 minutos10:00-12:00\ -+#ReceptivoE-mailNegócioOutras agênciasCobrançaNãoAté 15 minutos10:00-12:00T
 3#AtivoE-mailServiçoPoupadorCobrançaNãoAcima de 15 minutos10:00-12:00f	 );+#AtivoTelefoneDirecionamentoPoupadorConta corrente/PoupadorNãoAté 15 minutos15:00-17:00\ )))#ReceptivoVisitaDirecionamentoNão associadoOutrosNãoAté 5 minutos10:00-12:00s -)+)#ReceptivoWhatsappNegócioOutras agênciasCrédito geralSimCanais digitaisSimAté 5 minutos08:00-10:00q )))3#AtivoTelefoneNegócioNão associadoCrédito geralSimCrédito geralSimAcima de 15 minutos10:00-12:00n !3!')#AtivoPresencialServiçoOutras cooperativasConsórcioSimInvestimentosSimAté 5 minutos15:00-17:00v 39)#ReceptivoWhatsappServiçoOutras cooperativasSeguros e previdênciaSimSegurosSimAté 5 minutos15:00-17:00h )-+3#AtivoE-mailDirecionamentoOutras agênciasCanais digitaisNãoAcima de 15 minutos12:00-15:00n -++#	ReceptivoTelefoneNegócioOutras carteirasCartõesSimCanais digitaisNãoAté 15 minutos10:00-12:00p !);)#	AtivoPresencialServiçoMinha carteiraConta corrente/PoupadorSimCartõesSimAté 5 minutos08:00-10:00