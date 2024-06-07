from holded_dataflow import is_blacklisted
from apache_beam.io.gcp.pubsub import PubsubMessage

message = PubsubMessage(
    data=b"{\"id\":\"65e6f013ee1004565f0427a3\",\"accountId\":\"6374be699c11acaa3108cf02\",\"name\":\"Supervivientes Peleones Mazo de Commander - MTG: Universes Beyond Fallout\",\"description\":\"<h4>Supervivientes Peleones Mazo de Commander - MTG: Universes Beyond Fallout<\\/h4>\\r\\nLucha por la supervivencia contra otros yermenses con la llegada de la serie Fallout al formato para varios jugadores m\\u00e1s popular de Magic. Este bundle incluye\\u00a0<strong>los 4 mazos de Commander de Fallout<\\/strong>:\\u00a0<strong>1 Ave, C\\u00e9sar<\\/strong>\\u00a0(mazo rojo-blanco-negro),\\u00a0<strong>1 Supervivientes peleones<\\/strong>\\u00a0(mazo rojo-verde-blanco),\\u00a0<strong>1 \\u00a1Ciencia<\\/strong>! (mazo azul-blanco-rojo) y\\u00a0<strong>1 Amenaza mutante<\\/strong>\\u00a0(mazo negro-verde-azul).\\r\\n\\r\\nCada uno incluye 1 mazo listo para usar de 100 cartas de Magic (2 cartas legendarias foil tradicionales y 98 cartas no foil), un sobre de coleccionista de muestra (contiene 2 cartas foil tradicionales o no foil con tratamientos especiales, con 1 carta rara o de rareza superior con arte extendido y 1 carta poco com\\u00fan o de rareza superior con marco y arte alternativos), 1 comandante foil grabado especial (una copia de la carta de comandante en cartulina gruesa con un grabado foil en el borde y en la ilustraci\\u00f3n), 10 fichas de dos caras, 1 caja guardamazo (con capacidad para 100 cartas con protectores), 1 rueda de vidas, 1 hoja de estrategia y 1 tarjeta de referencia.\\r\\n<h4>Contenido<\\/h4>\\r\\n<ul>\\r\\n \\t<li>LOS REFUGIOS EST\\u00c1N ABIERTOS: viaja por los p\\u00e1ramos con cuatro mazos de 100 cartas, en cada uno de los cuales se incluyen cartas de Magic nunca vistas con personajes muy populares, mec\\u00e1nicas de juego tem\\u00e1ticas e ilustraciones que exploran el mundo posnuclear de la saga Fallout<\\/li>\\r\\n \\t<li>HAZTE CON LOS 4 MAZOS DE COMMANDER DE FALLOUT: este bundle incluye los 4 mazos de Commander de Magic: The Gathering\\u2014Fallout, con 1 mazo Ave, C\\u00e9sar, 1 mazo Supervivientes peleones, 1 mazo \\u00a1Ciencia! y 1 mazo Amenaza mutante<\\/li>\\r\\n \\t<li>LUCHA POR LA SUPERVIVENCIA CONTRA OTROS YERMENSES: lucha con amigos en juegos de MTG \\u00e9picos de entre 3 y 5 jugadores llenos de jugadas estrat\\u00e9gicas e intriga social; con estos mazos preconstruidos, listos para jugar nada m\\u00e1s abrirlos, podr\\u00e1s pasar a la acci\\u00f3n directamente<\\/li>\\r\\n \\t<li>COLECCIONA TRATAMIENTOS DE CARTAS DE FALLOUT ESPECIALES: cada mazo incluye un sobre de coleccionista con muestras que contiene 2 cartas especiales con marco alternativo, incluida 1 carta rara o rara m\\u00edtica<\\/li>\\r\\n \\t<li>TODO LO QUE NECESITAS PARA JUGAR Y M\\u00c1S TODAV\\u00cdA: cada mazo tambi\\u00e9n viene con 10 fichas de dos caras, 1 contador de vidas, 1 gu\\u00eda de estrategia y 1 caja guardamazo (con capacidad para 100 cartas con protectores)<\\/li>\\r\\n \\t<li>UN JUEGO QUE FUSIONA ARTE, HISTORIAS Y ESTRATEGIA: Magic: The Gathering es un juego de cartas coleccionables en el que la estrategia, el arte y las mec\\u00e1nicas se unen para explorar las tem\\u00e1ticas de diversos mundos y su historia; tanto si te interesa disfrutar de juegos casuales con tus amigos, coleccionar cartas incre\\u00edbles o lanzarte al panorama competitivo, Magic te da la bienvenida<\\/li>\\r\\n<\\/ul>\",\"kind\":\"simple\",\"barcode\":null,\"stock\":0,\"price\":\"49.54546\",\"cost\":null,\"weight\":0,\"sku\":\"5010996147097-Supervivientes\",\"factoryCode\":\"\",\"tags\":[],\"typeId\":null,\"origin\":{\"provider\":\"woocommerce\",\"providerId\":\"https:\\/\\/herofreaks.com\",\"originId\":\"87527\",\"extra\":[]},\"taxes\":[\"s_iva_21\"],\"purchaseTaxes\":[],\"appliedTaxes\":[{\"total\":\"59.95001\",\"amount\":\"10.40455\",\"base\":\"49.54546\",\"key\":\"s_iva_21\",\"group\":false}],\"attributes\":[],\"rates\":[],\"hasStock\":true,\"category\":null,\"forSale\":true,\"forPurchase\":true,\"salesAccount\":\"\",\"purchasesAccount\":\"\",\"warehouseId\":\"6374be6e9c11acaa3108cfc0\",\"version\":0,\"image\":false,\"urlImages\":[\"https:\\/\\/herofreaks.com\\/wp-content\\/uploads\\/2024\\/02\\/Supervivientes-Peleones-Universes-Beyond-Fallout.jpg\"],\"images\":null,\"inCatalog\":false,\"inPos\":null,\"flash\":[\"Supervivientes Peleones Mazo de Commander - MTG: Universes Beyond Fallout\",0,\"5010996147097-Supervivientes\",\"\",\"5010996147097-Supervivientes\"],\"originProvider\":\"woocommerce\",\"optionsList\":[],\"variants\":{\"class\":\"Holded\\\\Product\\\\Domain\\\\Product\\\\Simple\\\\SimpleVariants\",\"0\":{\"id\":\"65e6f013ee1004565f0427a4\"}},\"purchasePrices\":[]}",
    attributes={
    "X-Message-Stamp-Symfony\\Component\\Messenger\\Stamp\\BusNameStamp": "[{\"busName\":\"event.bus\"}]",
    "type": "Holded\\Product\\Domain\\Product\\Events\\ProductCreatedEvent",
    "Content-Type": "application/json",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\CorrelationIdStamp": "[{\"id\":\"01hr71kjjn5d6zhzgjsr6eqh36\"}]",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\ContextStamp": "[{\"accountId\":\"6374be699c11acaa3108cf02\",\"userId\":null,\"platform\":null,\"correlationId\":\"01hr71kjjn5d6zhzgjsr6eqh36\"}]",
    "targetSubscription": "Product",
    "X-Message-Stamp-Holded\\Core\\Messaging\\Messenger\\Stamp\\TimestampStamp": "[{\"dispatchedAt\":\"2024-03-05T10:12:35+00:00\"}]",
    "X-Message-Stamp-Holded\\Shared\\Infrastructure\\Messenger\\Stamp\\NewContextStamp": "[{\"actor\":{\"id\":\"65d345ca96f30a7b8f099689\",\"type\":\"api_key\"},\"accountId\":\"6374be699c11acaa3108cf02\",\"generatedBy\":\"api_key_to_context\"}]",
    "X-Message-Stamp-Holded\\Core\\Messaging\\Messenger\\Stamp\\MessageIdStamp": "[{\"id\":\"01hr71kjry3w47epk7acq7emcd\"}]",
    "X-Message-Stamp-Symfony\\Component\\Messenger\\Stamp\\HandledStamp": "[{\"result\":null,\"handlerName\":\"Holded\\\\Product\\\\Application\\\\HistoricalCost\\\\CreateHistoricalCostOnProductCreatedEventHandler::__invoke\"},{\"result\":null,\"handlerName\":\"Holded\\\\Product\\\\Application\\\\Product\\\\CounterUsage\\\\IncreaseCounterOnProductCreatedEventHandler::__invoke\"}]"
  }
)
event_name = message.attributes["type"]
if is_blacklisted(event_name, "PIPELINE"):
    print(f"Event: {event_name}, Filter Type: PIPELINE")
else:
    print("Not in PIPELINE")

if is_blacklisted(event_name, "SSGTM"):
    print(f"Event: {event_name}, Filter Type: SSGTM")
else:
    print("Not in SSGTM")