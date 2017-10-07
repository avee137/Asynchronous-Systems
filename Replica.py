# -*- generated by 1.0.9 -*-
import da
PatternExpr_205 = da.pat.TuplePattern([da.pat.ConstantPattern('PERFORM_OPERATION')])
PatternExpr_210 = da.pat.BoundPattern('_BoundPattern214_')
PatternExpr_227 = da.pat.TuplePattern([da.pat.ConstantPattern('SHUTTLE'), da.pat.ConstantPattern('REVERSE')])
PatternExpr_234 = da.pat.BoundPattern('_BoundPattern238_')
PatternExpr_271 = da.pat.TuplePattern([da.pat.ConstantPattern('SHUTTLE'), da.pat.ConstantPattern('FORWARD')])
PatternExpr_278 = da.pat.BoundPattern('_BoundPattern282_')
PatternExpr_346 = da.pat.ConstantPattern('')
PatternExpr_350 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.ConstantPattern('')])
_config_object = {}

class Replica(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ReplicaReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_0', PatternExpr_205, sources=[PatternExpr_210], destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_204]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_1', PatternExpr_227, sources=[PatternExpr_234], destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_226]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_2', PatternExpr_271, sources=[PatternExpr_278], destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_270]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_3', PatternExpr_346, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, client, olympus, currentReplica, prevReplica, nextReplica, **rest_359):
        super().setup(client=client, olympus=olympus, currentReplica=currentReplica, prevReplica=prevReplica, nextReplica=nextReplica, **rest_359)
        self._state.client = client
        self._state.olympus = olympus
        self._state.currentReplica = currentReplica
        self._state.prevReplica = prevReplica
        self._state.nextReplica = nextReplica
        print('****************setting up replica start*******************')
        self._state.client = self._state.client
        self._state.olympus = self._state.olympus
        self._state.currentReplica = self._state.currentReplica
        self._state.prevReplica = self._state.prevReplica
        self._state.nextReplica = self._state.nextReplica
        print('****************setting up replica finished****************')

    def run(self):
        self.output('********RUN : Received Message from Client. Replica Name : ', self._state.currentReplica, ' ********')
        super()._label('_st_label_343', block=False)
        _st_label_343 = 0
        while (_st_label_343 == 0):
            _st_label_343 += 1
            if PatternExpr_350.match_iter(self._ReplicaReceivedEvent_3, SELF_ID=self._id):
                _st_label_343 += 1
            else:
                super()._label('_st_label_343', block=True)
                _st_label_343 -= 1

    def main(self):
        pass

    def _Replica_handler_204(self):
        self.output('Reaching the head node! shuttle initiated:')
        self.send(('SHUTTLE', 'FORWARD'), to=self._state.nextReplica)
    _Replica_handler_204._labels = None
    _Replica_handler_204._notlabels = None

    def _Replica_handler_226(self):
        self.output('currentReplica: ', self._state.currentReplica, ', prevReplica: ', self._state.prevReplica, ', nextReplica: ', self._state.nextReplica, ', client: ', self._state.client, ', flag : REVERSE')
        if (self._state.prevReplica == None):
            self.output('***************YEAH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            self.send(('SHUTTLE', 'REVERSE'), to=self._state.prevReplica)
    _Replica_handler_226._labels = None
    _Replica_handler_226._notlabels = None

    def _Replica_handler_270(self):
        self.output('currentReplica: ', self._state.currentReplica, ', prevReplica: ', self._state.prevReplica, ', nextReplica: ', self._state.nextReplica, ', client: ', self._state.client, ', flag : FORWARD')
        if (self._state.nextReplica == None):
            self.output('recieved at tail, sending back ')
            self.send(('SHUTTLE',), to=self._state.client)
            self.send(('SHUTTLE', 'REVERSE'), to=self._state.prevReplica)
            self.output('sent to previous replca from tail')
        else:
            self.send(('SHUTTLE', 'FORWARD'), to=self._state.nextReplica)
            self.output('sent from replica', self._state.currentReplica)
    _Replica_handler_270._labels = None
    _Replica_handler_270._notlabels = None
