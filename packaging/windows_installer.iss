; SolidCraft 3D CAD 繁體中文版 Windows 安裝精靈設定檔
; 適用於 Inno Setup 6+

#define MyAppName "SolidCraft 3D CAD"
#define MyAppVersion "0.22.1"
#define MyAppPublisher "SolidCraft Contributors"
#define MyAppURL "https://github.com/bherbruck/solidcraft"
#define MyAppExeName "solidcraft.exe"
#define MyAppCliName "solidcraft-cli.exe"

[Setup]
AppId={{E6F7A8B9-C0D1-4E2F-A3B4-C5D6E7F8091A}
AppName={#MyAppName} (繁體中文版)
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\SolidCraft
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=..\dist
OutputBaseFilename=SolidCraft-v0.22.1-繁體中文安裝檔
SetupIconFile=..\assets\icons\app\windows\exports\solidcraft-executable.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
ChangesEnvironment=yes
ChangesAssociations=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "addtopath"; Description: "將 SolidCraft 加入系統 PATH 環境變數 (方便在終端機直接輸入 solidcraft)"; GroupDescription: "系統整合設定:"

[Files]
Source: "..\solidcraft.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\solidcraft-cli.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\啟動SolidCraft.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\SolidCraft_3D_CAD_繁體中文使用說明書.docx"; DestDir: "{app}"; Flags: ignoreversion isreadme
Source: "..\繁體中文使用說明.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\assets\icons\app\windows\exports\solidcraft-executable.ico"; DestDir: "{app}"; DestName: "solidcraft.ico"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\solidcraft.ico"
Name: "{group}\SolidCraft 命令列工具 (CLI)"; Filename: "{cmd}"; Parameters: "/K ""{app}\{#MyAppCliName}"" --help"; IconFilename: "{app}\solidcraft.ico"
Name: "{group}\繁體中文使用說明書 (Word)"; Filename: "{app}\SolidCraft_3D_CAD_繁體中文使用說明書.docx"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName} (繁體中文)"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\solidcraft.ico"; Tasks: desktopicon

[Registry]
; 註冊 .solidcraft 檔案關聯
Root: HKA; Subkey: "Software\Classes\.solidcraft"; ValueType: string; ValueName: ""; ValueData: "SolidCraft.Design"; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\.solidcraft"; ValueType: string; ValueName: "Content Type"; ValueData: "application/x-solidcraft"; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\SolidCraft.Design"; ValueType: string; ValueName: ""; ValueData: "SolidCraft 3D CAD 設計檔案"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\SolidCraft.Design\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\SolidCraft.Design\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

; 加入使用者 PATH 環境變數
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Tasks: addtopath; Check: NeedsAddPath(ExpandConstant('{app}'))

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', OrigPath)
  then begin
    Result := True;
    exit;
  end;
  Result := Pos(';' + UpperCase(Param) + ';', ';' + UpperCase(OrigPath) + ';') = 0;
end;
