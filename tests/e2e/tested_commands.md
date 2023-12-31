# Commands to test

## Key

  X: Has specific test which is passing
  F: Has a test in some form, for example in the setup
  S: Currently skipping the test due to a failure

  Empty boxes mean no test exists currently

## Commands

### Misc

 [F] AuthenticateCommand
 [F] ChangeSessionIdCommand
 [X] GetTimestampCommand
 [S] DisconnectAndExitCommand
 [S] ReconnectToTheServerCommand
 [X] LogDebugToConsoleCommand
 [X] LogDebugToConsoleTranslatedCommand
 [X] LogToConsoleCommand
 [X] LogToConsoleTranslatedCommand
 [X] RunScriptCommand
 [X] SendAnimationCommand

### Inventory

 [X] ChangeSlotCommand
 [S] ClearInventoriesCommand - Seems to not work as expected, clears "Opened" inventories
 [X] GetCurrentSlotCommand
 [ ] GetInventoriesCommand
 [X] GetInventoryEnabledCommand
 [X] GetPlayerInventoryCommand
 [ ] CloseInventoryCommand
 [ ] CreativeDeleteCommand
 [ ] CreativeGiveCommand
 [ ] SetSlotCommand
 [ ] WindowActionCommand

### Entities

 [S] GetEntitiesCommand
 [X] GetEntityHandlingEnabledCommand
 [ ] InteractEntityCommand
 [ ] SelectTradeCommand
 [ ] SendEntityActionCommand

### Player

 [X] GetGamemodeCommand
 [X] GetPlayersLatencyCommand
 [X] GetUserUUIDCommand
 [X] GetUsernameCommand
 [S] RespawnCommand

### Server

 [X] GetMaxChatMessageLengthCommand
 [X] GetOnlinePlayersCommand
 [X] GetOnlinePlayersWithUUIDCommand
 [X] GetServerHostCommand
 [X] GetServerPortCommand
 [X] GetServerTPSCommand

### World

 [X] GetTerrainEnabledCommand
 [X] GetWorldCommand
 [ ] DigBlockCommand
 [ ] SendPlaceBlockCommand
 [ ] UpdateSignCommand
 [ ] UpdateCommandBlockCommand

### Movement

 [X] ClientIsMovingCommand
 [F] MoveToLocationCommand
 [X] GetCurrentLocationCommand
 [X] GetPitchCommand
 [X] GetYawCommand
 [ ] LookAtLocationCommand
 [ ] SetTerrainEnabledCommand
 [ ] SneakCommand
 [ ] UseItemInHandCommand

## Future test improvements

 [ ] GetPlayerInventoryCommand: Test whether the inventory can be moved etc
