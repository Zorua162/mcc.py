# Import commands
from mcc.commands.GetPitchCommand import GetPitchCommand
from mcc.commands.GetTerrainEnabledCommand import GetTerrainEnabledCommand
from mcc.commands.ChangeSessionIdCommand import ChangeSessionIdCommand
from mcc.commands.RespawnCommand import RespawnCommand
from mcc.commands.LookAtLocationCommand import LookAtLocationCommand
from mcc.commands.GetYawCommand import GetYawCommand
from mcc.commands.GetServerTPSCommand import GetServerTPSCommand
from mcc.commands.GetCurrentSlotCommand import GetCurrentSlotCommand
from mcc.commands.MoveToLocationCommand import MoveToLocationCommand
from mcc.commands.InteractEntityCommand import InteractEntityCommand
from mcc.commands.GetCurrentLocationCommand import GetCurrentLocationCommand
from mcc.commands.GetPlayersLatencyCommand import GetPlayersLatencyCommand
from mcc.commands.AuthenticateCommand import AuthenticateCommand
from mcc.commands.GetServerHostCommand import GetServerHostCommand
from mcc.commands.UpdateSignCommand import UpdateSignCommand
from mcc.commands.GetInventoriesCommand import GetInventoriesCommand
from mcc.commands.SetSlotCommand import SetSlotCommand
from mcc.commands.ChangeSlotCommand import ChangeSlotCommand
from mcc.commands.GetOnlinePlayersCommand import GetOnlinePlayersCommand
from mcc.commands.LogDebugToConsoleTranslatedCommand import (
    LogDebugToConsoleTranslatedCommand,
)
from mcc.commands.CreativeGiveCommand import CreativeGiveCommand
from mcc.commands.UpdateCommandBlockCommand import UpdateCommandBlockCommand
from mcc.commands.GetUsernameCommand import GetUsernameCommand
from mcc.commands.GetTimestampCommand import GetTimestampCommand
from mcc.commands.GetOnlinePlayersWithUUIDCommand import GetOnlinePlayersWithUUIDCommand
from mcc.commands.GetGamemodeCommand import GetGamemodeCommand
from mcc.commands.ReconnectToTheServerCommand import ReconnectToTheServerCommand
from mcc.commands.ClearInventoriesCommand import ClearInventoriesCommand
from mcc.commands.CreativeDeleteCommand import CreativeDeleteCommand
from mcc.commands.LogDebugToConsoleCommand import LogDebugToConsoleCommand
from mcc.commands.LogToConsoleCommand import LogToConsoleCommand
from mcc.commands.SelectTradeCommand import SelectTradeCommand
from mcc.commands.SendAnimationCommand import SendAnimationCommand
from mcc.commands.GetInventoryEnabledCommand import GetInventoryEnabledCommand
from mcc.commands.GetWorldCommand import GetWorldCommand
from mcc.commands.CloseInventoryCommand import CloseInventoryCommand
from mcc.commands.DigBlockCommand import DigBlockCommand
from mcc.commands.GetPlayerInventoryCommand import GetPlayerInventoryCommand
from mcc.commands.LogToConsoleTranslatedCommand import LogToConsoleTranslatedCommand
from mcc.commands.RunScriptCommand import RunScriptCommand
from mcc.commands.DisconnectAndExitCommand import DisconnectAndExitCommand
from mcc.commands.GetServerPortCommand import GetServerPortCommand
from mcc.commands.GetEntitiesCommand import GetEntitiesCommand
from mcc.commands.GetMaxChatMessageLengthCommand import GetMaxChatMessageLengthCommand
from mcc.commands.SendEntityActionCommand import SendEntityActionCommand
from mcc.commands.UseItemInHandCommand import UseItemInHandCommand
from mcc.commands.GetEntityHandlingEnabledCommand import GetEntityHandlingEnabledCommand
from mcc.commands.WindowActionCommand import WindowActionCommand
from mcc.commands.SendPlaceBlockCommand import SendPlaceBlockCommand
from mcc.commands.GetUserUUIDCommand import GetUserUUIDCommand
from mcc.commands.ClientIsMovingCommand import ClientIsMovingCommand
from mcc.commands.SetTerrainEnabledCommand import SetTerrainEnabledCommand
from mcc.commands.SneakCommand import SneakCommand


class ChatBot:
    # Event methods

    def OnWsCommandResponse(self, success, requestId, command, result):
        # place holder event
        pass

    def OnBlockBreakAnimation(self, Entity, Location, stage):
        # place holder event
        pass

    def OnEntityAnimation(self, Entity, animation):
        # place holder event
        pass

    def OnChatPrivate(self, sender, message, rawText):
        # place holder event
        pass

    def OnChatPublic(self, username, message, rawText):
        # place holder event
        pass

    def OnTeleportRequest(self, sender, rawText):
        # place holder event
        pass

    def OnChatRaw(self, text, json):
        # place holder event
        pass

    def OnDisconnect(self, reason, message):
        # place holder event
        pass

    def OnPlayerProperty(self, prop):
        # place holder event
        pass

    def OnServerTpsUpdate(self, tps):
        # place holder event
        pass

    def OnTimeUpdate(self, worldAge, timeOfDay):
        # place holder event
        pass

    def OnEntityMove(self, *Entity):
        # place holder event
        pass

    def OnInternalCommand(self, command, parameters, result):
        # place holder event
        pass

    def OnEntitySpawn(self, *Entity):
        # place holder event
        pass

    def OnEntityDespawn(self, *Entity):
        # place holder event
        pass

    def OnHeldItemChange(self, OnHeldItemChange):
        # place holder event
        pass

    def OnHealthUpdate(self, OnHealthUpdate, health):
        # place holder event
        pass

    def OnExplosion(self, OnExplosion, Location, strength):
        # place holder event
        pass

    def OnSetExperience(self, OnSetExperience, experienceBar, level):
        # place holder event
        pass

    def OnGamemodeUpdate(self, OnGamemodeUpdate, playerName, uuid):
        # place holder event
        pass

    def OnLatencyUpdate(self, OnLatencyUpdate, playerName, uuid):
        # place holder event
        pass

    def OnMapData(
        self,
        OnMapData,
        mapId,
        scale,
        trackingPosition,
        locked,
        icons,
        columnsUpdated,
        rowsUpdated,
        mapColumnX,
        mapRowZ,
    ):
        # place holder event
        pass

    def OnTradeList(self, OnTradeList, windowId, trades):
        # place holder event
        pass

    def OnTitle(
        self,
        OnTitle,
        action,
        titleText,
        subtitleText,
        actionBarText,
        fadeIn,
        stay,
        fadeout,
    ):
        # place holder event
        pass

    def OnEntityEquipment(self, OnEntityEquipment, Entity, slot):
        # place holder event
        pass

    def OnEntityEffect(self, OnEntityEffect, Entity, effect, amplifier, duration):
        # place holder event
        pass

    def OnScoreboardObjective(
        self, OnScoreboardObjective, objectiveName, mode, objectiveValue, type
    ):
        # place holder event
        pass

    def OnUpdateScore(self, OnUpdateScore, entityName, action, objectiveName):
        # place holder event
        pass

    def OnInventoryUpdate(self, OnInventoryUpdate):
        # place holder event
        pass

    def OnInventoryOpen(self, OnInventoryOpen):
        # place holder event
        pass

    def OnInventoryClose(self, OnInventoryClose):
        # place holder event
        pass

    def OnPlayerJoin(self, OnPlayerJoin, uuid):
        # place holder event
        pass

    def OnPlayerLeave(self, OnPlayerLeave, uuid):
        # place holder event
        pass

    def OnDeath(self):
        # place holder event
        pass

    def OnRespawn(self):
        # place holder event
        pass

    def OnEntityHealth(self, OnEntityHealth, Entity):
        # place holder event
        pass

    def OnEntityMetadata(self, OnEntityMetadata, Entity):
        # place holder event
        pass

    def OnPlayerStatus(self, OnPlayerStatus):
        # place holder event
        pass

    # Command methods

    def GetPitchCommand(self):
        return self.sendCommand(GetPitchCommand())

    def GetTerrainEnabledCommand(self):
        return self.sendCommand(GetTerrainEnabledCommand())

    def ChangeSessionIdCommand(self):
        return self.sendCommand(ChangeSessionIdCommand())

    def RespawnCommand(self):
        return self.sendCommand(RespawnCommand())

    def LookAtLocationCommand(self):
        return self.sendCommand(LookAtLocationCommand())

    def GetYawCommand(self):
        return self.sendCommand(GetYawCommand())

    def GetServerTPSCommand(self):
        return self.sendCommand(GetServerTPSCommand())

    def GetCurrentSlotCommand(self):
        return self.sendCommand(GetCurrentSlotCommand())

    def MoveToLocationCommand(self):
        return self.sendCommand(MoveToLocationCommand())

    def InteractEntityCommand(self):
        return self.sendCommand(InteractEntityCommand())

    def GetCurrentLocationCommand(self):
        return self.sendCommand(GetCurrentLocationCommand())

    def GetPlayersLatencyCommand(self):
        return self.sendCommand(GetPlayersLatencyCommand())

    def AuthenticateCommand(self):
        return self.sendCommand(AuthenticateCommand())

    def GetServerHostCommand(self):
        return self.sendCommand(GetServerHostCommand())

    def UpdateSignCommand(self):
        return self.sendCommand(UpdateSignCommand())

    def GetInventoriesCommand(self):
        return self.sendCommand(GetInventoriesCommand())

    def SetSlotCommand(self):
        return self.sendCommand(SetSlotCommand())

    def ChangeSlotCommand(self):
        return self.sendCommand(ChangeSlotCommand())

    def GetOnlinePlayersCommand(self):
        return self.sendCommand(GetOnlinePlayersCommand())

    def LogDebugToConsoleTranslatedCommand(self):
        return self.sendCommand(LogDebugToConsoleTranslatedCommand())

    def CreativeGiveCommand(self):
        return self.sendCommand(CreativeGiveCommand())

    def UpdateCommandBlockCommand(self):
        return self.sendCommand(UpdateCommandBlockCommand())

    def GetUsernameCommand(self):
        return self.sendCommand(GetUsernameCommand())

    def GetTimestampCommand(self):
        return self.sendCommand(GetTimestampCommand())

    def GetOnlinePlayersWithUUIDCommand(self):
        return self.sendCommand(GetOnlinePlayersWithUUIDCommand())

    def GetGamemodeCommand(self):
        return self.sendCommand(GetGamemodeCommand())

    def ReconnectToTheServerCommand(self):
        return self.sendCommand(ReconnectToTheServerCommand())

    def ClearInventoriesCommand(self):
        return self.sendCommand(ClearInventoriesCommand())

    def CreativeDeleteCommand(self):
        return self.sendCommand(CreativeDeleteCommand())

    def LogDebugToConsoleCommand(self):
        return self.sendCommand(LogDebugToConsoleCommand())

    def LogToConsoleCommand(self):
        return self.sendCommand(LogToConsoleCommand())

    def SelectTradeCommand(self):
        return self.sendCommand(SelectTradeCommand())

    def SendAnimationCommand(self):
        return self.sendCommand(SendAnimationCommand())

    def GetInventoryEnabledCommand(self):
        return self.sendCommand(GetInventoryEnabledCommand())

    def GetWorldCommand(self):
        return self.sendCommand(GetWorldCommand())

    def CloseInventoryCommand(self):
        return self.sendCommand(CloseInventoryCommand())

    def DigBlockCommand(self):
        return self.sendCommand(DigBlockCommand())

    def GetPlayerInventoryCommand(self):
        return self.sendCommand(GetPlayerInventoryCommand())

    def LogToConsoleTranslatedCommand(self):
        return self.sendCommand(LogToConsoleTranslatedCommand())

    def RunScriptCommand(self):
        return self.sendCommand(RunScriptCommand())

    def DisconnectAndExitCommand(self):
        return self.sendCommand(DisconnectAndExitCommand())

    def GetServerPortCommand(self):
        return self.sendCommand(GetServerPortCommand())

    def GetEntitiesCommand(self):
        return self.sendCommand(GetEntitiesCommand())

    def GetMaxChatMessageLengthCommand(self):
        return self.sendCommand(GetMaxChatMessageLengthCommand())

    def SendEntityActionCommand(self):
        return self.sendCommand(SendEntityActionCommand())

    def UseItemInHandCommand(self):
        return self.sendCommand(UseItemInHandCommand())

    def GetEntityHandlingEnabledCommand(self):
        return self.sendCommand(GetEntityHandlingEnabledCommand())

    def WindowActionCommand(self):
        return self.sendCommand(WindowActionCommand())

    def SendPlaceBlockCommand(self):
        return self.sendCommand(SendPlaceBlockCommand())

    def GetUserUUIDCommand(self):
        return self.sendCommand(GetUserUUIDCommand())

    def ClientIsMovingCommand(self):
        return self.sendCommand(ClientIsMovingCommand())

    def SetTerrainEnabledCommand(self):
        return self.sendCommand(SetTerrainEnabledCommand())

    def SneakCommand(self):
        return self.sendCommand(SneakCommand())
