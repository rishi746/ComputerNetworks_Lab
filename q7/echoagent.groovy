
import org.arl.fjage.*
import org.arl.unet.*

class EchoAgent extends UnetAgent {

    @Override
    void startup() {
        subscribe(topic(Topics.DATAGRAM))
        log.info('EchoAgent started')
    }

    @Override
    void processMessage(Message msg) {
        if (msg instanceof DatagramNtf &&
            msg.protocol == Protocol.USER) {

            def text = new String(msg.data as byte[], 'UTF-8')
            def receivedAt = System.currentTimeMillis()

            def replyText = text.toUpperCase() +
                " | Received at: ${receivedAt}"

            def payload = replyText.getBytes('UTF-8').collect {
                it & 0xff
            }

            send new DatagramReq(
                recipient: msg.sender,
                to: msg.from,
                protocol: Protocol.DATA,
                data: payload
            )
        }
    }
}
